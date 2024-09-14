from docplex.mp.model import Model
import numpy as np
import ctypes
from Matrix.EnergyMatrix import EnergyMatrix

class MIP():
    def __init__(self, uav, M):
        self.uav = uav
        self.energyMatrix = uav.energyMatrix
        self.costMatrix = uav.costMatrix
        self.M = M
        self.evList = uav.evList
        self.N = range(len(self.evList))
        self.N_1 = range(len(self.evList) - 1)
        self.q_realized = np.empty(len(self.N))
        
        self.x1 = np.empty([len(uav.evList)])
        self.x2 = np.empty([len(uav.evList)])
        self.y = np.empty([len(uav.evList)])
        self.z = np.empty([len(uav.evList)])
        self.q = np.empty([len(uav.evList)])
        self.obj = -9999
        self.feasible = True
    
    def RunMIP(self):
        md = Model('MIP for EVCG problem')
        
        # Decision variables
        X1 = ((i) for i in self.N)
        x1 = md.binary_var_dict(X1, name = 'x1', lb = 0)
        
        Y = ((i) for i in self.N)
        y = md.binary_var_dict(Y, name = 'y', lb = 0)
        
        Z = ((i) for i in self.N)
        z = md.binary_var_dict(Z, name = 'z', lb = 0)
        
        Q = ((i) for i in self.N)
        q = md.integer_var_dict(Q, name = 'q', lb = 0)
        
        
        # Objective function
        obj = sum(self.costMatrix.Cost_4[j, j+1] * x1[j] for j in self.N_1) + sum(((self.costMatrix.Cost_3[j] + self.costMatrix.Cost_2[j+1]) * y[j]) for j in self.N_1) + sum(((self.costMatrix.Cost_4[j, j+1] + self.uav.chargeFee) * z[j]) for j in self.N_1) + sum(self.costMatrix.Cost_3[j] * x1[j] for j in range(len(self.evList) - 1, len(self.evList))) + sum((self.uav.chargeFee + self.costMatrix.Cost_3[j]) * z[j] for j in range(len(self.evList) - 1, len(self.evList)))
        md.set_objective('min', obj)
        
        
        # Constraints
        # (D.1)
        md.add_constraint(q[0] <= (self.uav.capacity - self.energyMatrix.Energy_2[0] - self.evList[0].discretizedExpectedDemand))
        # md.add_constraint(q[0] <= (self.uav.capacity - self.energyMatrix.Energy_2[0] - self.evList[0].discretizedElectricityDemandMin))
        # md.add_constraint(q[0] <= (self.uav.capacity - self.energyMatrix.Energy_2[0] - self.evList[0].discretizedElectricityDemandMax))
        
        
        # (D.2)
        for j in self.N_1:
            md.add_constraint(md.if_then(x1[j] == 1, (q[j+1] <= (q[j] - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].discretizedExpectedDemand))))
            # md.add_constraint(md.if_then(x1[j] == 1, (q[j+1] <= (q[j] - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].discretizedElectricityDemandMin))))
            # md.add_constraint(md.if_then(x1[j] == 1, (q[j+1] <= (q[j] - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].discretizedElectricityDemandMax))))
            
        
        # (D.3)
        for j in self.N_1:
            md.add_constraint(md.if_then(y[j] == 1, (q[j+1] <= (self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].discretizedExpectedDemand))))
            # md.add_constraint(md.if_then(y[j] == 1, (q[j+1] <= (self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].discretizedElectricityDemandMin))))
            # md.add_constraint(md.if_then(y[j] == 1, (q[j+1] <= (self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].discretizedElectricityDemandMax))))
            
        
        # (D.4)
        for j in self.N_1:
            md.add_constraint(md.if_then(z[j] == 1, (q[j+1] <= (self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].discretizedExpectedDemand))))
            # md.add_constraint(md.if_then(z[j] == 1, (q[j+1] <= (self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].discretizedElectricityDemandMin))))
            # md.add_constraint(md.if_then(z[j] == 1, (q[j+1] <= (self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].discretizedElectricityDemandMax))))
            
        
        
        # (D.5)
        for j in self.N_1:
            md.add_constraint(md.if_then(x1[j] == 1, (q[j] >= (self.energyMatrix.Energy_4[j, j+1] + self.evList[j+1].discretizedExpectedDemand))))
            # md.add_constraint(md.if_then(x1[j] == 1, (q[j] >= (self.energyMatrix.Energy_4[j, j+1] + self.evList[j+1].discretizedElectricityDemandMin))))
            # md.add_constraint(md.if_then(x1[j] == 1, (q[j] >= (self.energyMatrix.Energy_4[j, j+1] + self.evList[j+1].discretizedElectricityDemandMax))))
        
        # (D.6)
        for j in self.N_1:
            md.add_constraint(md.if_then(x1[j] == 1, (q[j] >= (self.energyMatrix.Energy_4[j, j+1] + self.energyMatrix.Energy_2[j+1]))))
        
        # (D.7)
        for j in self.N_1:
            md.add_constraint(md.if_then(y[j] == 1, (q[j] >= (self.energyMatrix.Energy_3[j]))))
        
        # (D.8)
        for j in self.N_1:
            md.add_constraint(md.if_then(x1[len(self.evList) - 1] == 1, (q[len(self.evList) - 1] >= (self.energyMatrix.Energy_3[len(self.evList) - 1]))))
        
        
        
        # (D.9)
        md.add_constraints((x1[j] + y[j] + z[j]) == 1 for j in self.N_1)
        
        # (D.10)
        md.add_constraint(y[len(self.evList) - 1] == 0)
        
        
        # (D.11)
        md.add_constraint((x1[len(self.evList) - 1] + z[len(self.evList) - 1]) == 1)
        
        
        # (D.12)
        md.add_constraints((x1[j] + y[j] + z[j]) >= (x1[j+1] + y[j+1] + z[j+1]) for j in self.N_1)
        
        # (D.13)
        md.add_constraints(q[j] <= self.uav.capacity for j in self.N)
        
        # Run
        md.solve(log_output=True)
        # print(md.export_as_lp_string())
        # print(md.solve_details)
        # print(md.solution)
        # print("Solution status  :  " , md.get_solve_status())
        # print("Objective value  :  " , md.objective_value)
        # print("Solution value  :  " , obj.solution_value)
        
        
        
        # Initialize solution list
        self.x1 = [0 for i in range(len(self.uav.evList))]
        self.x2 = [0 for i in range(len(self.uav.evList))]
        self.y = [0 for i in range(len(self.uav.evList))]
        self.z = [0 for i in range(len(self.uav.evList))]
        self.q = [0 for i in range(len(self.uav.evList))]
        
        
        
        # Save solutions
        for j in self.N:
            self.x1[j] =  int(round(x1[j].solution_value))
            self.y[j] = int(round(y[j].solution_value))
            self.z[j] = int(round(z[j].solution_value))
            self.q[j] = int(round(q[j].solution_value))
        
        
        '''
        # MIP verification
        flag = self.MIPVerification()
        
        if(flag == False):
            ctypes.windll.user32.MessageBoxW(0, "Something goes wrong in MIP", "Error", 1)
            quit()
        '''
        
        
        # Reflect the realized demand
        self.q_realized[0] = self.uav.capacity - self.energyMatrix.Energy_2[0] - self.evList[0].realizedDemand
        
        
        for j in self.N_1:
            # update the solution
            if(self.x1[j] == 1):
                
                '''
                if(self.q_realized[j] < self.energyMatrix.Energy_4[j, j+1] + self.energyMatrix.Energy_2[j+1]):
                    if(self.q_realized[j] < self.energyMatrix.Energy_3[j]):
                            self.x1[j] = 0
                            self.z[j] = 1
                    else:
                        if(self.costMatrix.Cost_3[j] + self.costMatrix.Cost_2[j+1] >= self.costMatrix.Cost_4[j, j+1] + self.uav.chargeFee):
                            self.x1[j] = 0
                            self.z[j] = 1
                        else:
                            self.x1[j] = 0
                            self.y[j] = 1
                '''        
                # elif(self.q_realized[j] - self.energyMatrix.Energy_4[j, j+1] < self.evList[j+1].realizedDemand):
                if(self.q_realized[j] - self.energyMatrix.Energy_4[j, j+1] < self.evList[j+1].realizedDemand):
                    if(self.q_realized[j] - self.energyMatrix.Energy_4[j, j+1] >= self.energyMatrix.Energy_2[j+1]):
                        self.x1[j] = 0
                        self.x2[j] = 1
                    else:
                        self.x1[j] = 0
                        self.x2[j] = 1
                        self.feasible = False
                        self.iter = j
                        break
   
                
            elif(self.y[j] == 1):
                if(self.q_realized[j] < self.energyMatrix.Energy_3[j]):
                    self.y[j] = 0
                    self.z[j] = 1    
            
                
            
            # realized remainig energy update
            if (self.x1[j] == 1):
                self.q_realized[j+1] = self.q_realized[j] - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].realizedDemand
            elif (self.x2[j] == 1):
                self.q_realized[j+1] = self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].realizedDemand
            elif (self.y[j] == 1):
                self.q_realized[j+1] = self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].realizedDemand
            elif (self.z[j] == 1):
                self.q_realized[j+1] = self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].realizedDemand
        
        
        if(self.feasible):
            # last node
            if (self.q_realized[len(self.evList) - 1] < self.energyMatrix.Energy_3[len(self.evList) - 1]):
                self.x1[len(self.evList) - 1] = 0
                self.x2[len(self.evList) - 1] = 0
                self.y[len(self.evList) - 1] = 0
                self.z[len(self.evList) - 1] = 1
            else:
                self.x1[len(self.evList) - 1] = 1
                self.x2[len(self.evList) - 1] = 0
                self.y[len(self.evList) - 1] = 0
                self.z[len(self.evList) - 1] = 0
            
            # objective value
            self.obj = self.ObjectiveValue()

        if(self.feasible == False):
            for j in range(self.iter + 1, len(self.N)):
                self.x1[j] = -9999
                self.x2[j] = -9999
                self.y[j] = -9999
                self.z[j] = -9999
                self.q[j] = -9999
    
        return (self.x1, self.x2, self.y, self.z, self.q_realized, self.obj, self.feasible)
    
    
    def ObjectiveValue(self):
        objValue = 0.0
        objValue = objValue + self.costMatrix.Cost_2[0]
        
        for i in self.N:
            if self.x1[i] == 1:    
                if(i != len(self.N) - 1):
                    objValue = objValue + self.costMatrix.Cost_4[i, i+1]
                else:
                    objValue = objValue + self.costMatrix.Cost_3[i]
                
            elif self.x2[i] == 1:
                # objValue = objValue + self.costMatrix.Cost_4[i, i+1] + (2 * self.costMatrix.Cost_2[i+1]) + self.uav.routeFailureCost
                objValue = objValue + self.costMatrix.Cost_4[i, i+1] + (2 * self.costMatrix.Cost_2[i+1])
                
            elif self.y[i] == 1:
                objValue = objValue + self.costMatrix.Cost_3[i] + self.costMatrix.Cost_2[i+1]
                
            elif self.z[i] == 1:
                if(i != len(self.N) - 1):
                    objValue = objValue + self.costMatrix.Cost_4[i][i+1] + self.uav.chargeFee
                else:
                    objValue = objValue + self.costMatrix.Cost_3[i] + self.uav.chargeFee
            
        return objValue



    def MIPVerification(self):
        remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_2[0] - self.evList[0].discretizedExpectedDemand
        
        flag = True
        for j in self.N_1:
            if (self.x1[j] == 1):
                remainingEnergy = remainingEnergy - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].discretizedExpectedDemand
                
            elif (self.x2[j] == 1):
                if(remainingEnergy - self.energyMatrix.Energy_4[j, j+1] - self.energyMatrix.Energy_2[j+1] < 0):
                    flag = False
                    break
                remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].discretizedExpectedDemand
                
            elif (self.y[j] == 1):
                if(remainingEnergy - self.energyMatrix.Energy_3[j] < 0):
                    flag = False
                    break
                remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].discretizedExpectedDemand
                
            elif (self.z[j] == 1):
                remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].discretizedExpectedDemand
                
            if((self.q[j+1] != remainingEnergy) or (remainingEnergy < 0)):
                flag = False
                break
        
        if(flag):    
            if(self.x1[len(self.N_1)] == 1):
                if(remainingEnergy - self.energyMatrix.Energy_3[len(self.N_1)] < 0):
                    flag = False
                
        return flag