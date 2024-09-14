from audioop import reverse
import numpy as np
import ctypes


class DynamicPrograming():
    def __init__(self, uav, M):
        self.uav = uav
        self.M = M
        self.f_array = np.zeros([len(uav.evList), uav.capacity + 1])   # number of EVs x uav's capacity
        self.f_array_policy = np.zeros([len(uav.evList), uav.capacity + 1])   # number of EVs x uav's capacity
        
        self.x_array = np.empty([len(uav.evList), uav.capacity + 1])   # x[j, q] = 0 (Eq. 1.1), 1 (Eq. 1.2), or 2 (Eq. 1.3)
        self.x_array.fill(100000000)
        
        self.x_array_policy = np.empty([len(uav.evList), uav.capacity + 1])   # x[j, q] = 0 (Eq. 1.1), 1 (Eq. 1.2), or 2 (Eq. 1.3)
        self.x_array_policy.fill(100000000) 
         
        self.solution = []
        self.solution_policy = []
        self.q = np.empty([len(uav.evList)])
        
        self.thresholdList_1 = np.empty([len(uav.evList) - 1, 2]) # c_(j^-,0) + c_(0,(j+1)^+) ≤ c_c + c_(j^-,(j+1)^+) case, [][0] = e_(j^-,0), [][1] = h_j (skip the last EV for finding thresholds)
        self.thresholdList_1.fill(-9999)
        
        self.thresholdList_2 = np.empty([len(uav.evList) - 1, 1]) # c_(j^-,0) + c_(0,(j+1)^+) > c_c + c_(j^-,(j+1)^+) case, [][0] = h_j (skip the last EV for finding thresholds)
        self.thresholdList_2.fill(-9999)
      
        self.evList = uav.evList
        self.energyMatrix = uav.energyMatrix
        self.costMatrix = uav.costMatrix
        self.odMatrix = uav.odMatrix
    
    def ObjectiveValue(self, solution):
        q = self.uav.capacity
        objValue = 0.0
        
        q = q - self.energyMatrix.Energy_2[0]
        q = q - self.evList[0].realizedDemand
        objValue = objValue + self.costMatrix.Cost_2[0]
        
        for i in range(len(solution) - 1):
            if solution[i] == 0:
                if self.energyMatrix.Energy_4[i, i+1] + self.evList[i+1].realizedDemand <= q:
                    q = q - self.energyMatrix.Energy_4[i, i+1] - self.evList[i+1].realizedDemand
                    objValue = objValue + self.costMatrix.Cost_4[i, i+1]
                else:
                    q = self.uav.capacity - self.energyMatrix.Energy_2[i+1] - self.evList[i+1].realizedDemand
                    objValue = objValue + self.costMatrix.Cost_4[i, i+1] + (2 * self.costMatrix.Cost_2[i+1]) + self.uav.routeFailureCost
                
            elif solution[i] == 1:
                q = self.uav.capacity - self.energyMatrix.Energy_2[i+1] - self.evList[i+1].realizedDemand
                objValue = objValue + self.costMatrix.Cost_3[i] + self.costMatrix.Cost_2[i+1]
                
            elif solution[i] == 2:
                q = self.uav.capacity - self.energyMatrix.Energy_4[i][i+1] - self.evList[i+1].realizedDemand
                objValue = objValue + self.costMatrix.Cost_4[i][i+1] + self.uav.chargeFee
        
        if q >= self.energyMatrix.Energy_3[len(solution) - 1]:
            objValue = objValue + self.costMatrix.Cost_3[len(solution) - 1]
        else:
            objValue = objValue + self.costMatrix.Cost_3[len(solution) - 1] + self.uav.chargeFee
            
            
        return objValue



    
    def RunOptimalPolicy(self):
        remainingEnergy = self.uav.capacity
        # Find h_j
        for j in range(len(self.evList) - 1):
            if j == 0:
                remainingEnergy = remainingEnergy - self.energyMatrix.Energy_2[j] - self.evList[j].realizedDemand

            
            value2 = self.H2(j, self.energyMatrix.Energy_3[j])
            value3 = self.H3(j, self.energyMatrix.Energy_3[j])
            
            
            # Fig. 4
            if value3 < value2:
                
                value3 = self.H3_policy(j, remainingEnergy)
                
                for q in reversed(range(int(self.uav.capacity) + 1)):
                    value1 = self.H1(j, q)
                    if value1 > value3:
                        if(q + 1 <= self.uav.capacity):
                            self.uav.h[j] = q + 1
                        else:
                            self.uav.h[j] = self.uav.capacity
                        break
            
            
            # Fig. 5
            elif value3 >= value2:
                
                value2 = self.H2(j, self.uav.capacity)

                for q in reversed(range(int(self.uav.capacity) + 1)):
                    value1 = self.H1(j, q)
                    if value1 > value2:
                        if(q + 1 <= self.uav.capacity):
                            self.uav.h[j] = q + 1
                        else:
                            self.uav.h[j] = self.uav.capacity
                        break
                
            
            
        # save solution    
        #############
        remainingEnergy = self.uav.capacity
        x = 10000
        for j in range(len(self.evList) - 1):
            if j == 0:
                remainingEnergy = remainingEnergy - self.energyMatrix.Energy_2[j] - self.evList[j].realizedDemand
                self.q[j] = remainingEnergy

            value2 = self.H2(j, self.energyMatrix.Energy_3[j])
            value3 = self.H3(j, self.energyMatrix.Energy_3[j])
            
            # Fig. 4
            if value3 < value2:
                if remainingEnergy < self.uav.h[j]:
                    x = 2
                    self.solution_policy.append(x)
                
                else:
                    x = 0
                    self.solution_policy.append(x)
            
            
            
            # Fig. 5
            elif value3 >= value2:
                if remainingEnergy < self.energyMatrix.Energy_3[j]:
                    x = 2
                    self.solution_policy.append(x)
                
                elif remainingEnergy < self.uav.h[j]:
                    x = 1
                    self.solution_policy.append(x)
                        
                else:
                    x = 0
                    self.solution_policy.append(x)
                    
                
                
            # remaining energy update
            if x == 0:
                if remainingEnergy >= self.energyMatrix.Energy_4[j, j+1] + self.evList[j+1].realizedDemand:
                    remainingEnergy = remainingEnergy - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].realizedDemand
                    self.q[j+1] = remainingEnergy
                else:
                    remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].realizedDemand
                    self.q[j+1] = remainingEnergy
                
            elif x == 1:
                remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].realizedDemand
                self.q[j+1] = remainingEnergy
            
            elif x == 2:
                remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].realizedDemand
                self.q[j+1] = remainingEnergy
          
        # last ev
        if remainingEnergy < self.energyMatrix.Energy_3[len(self.evList) - 1]:
            x = 2
        else:
            x = 0
        self.solution_policy.append(x)
        
        if (len(self.evList) == 1):
            remainingEnergy = remainingEnergy - self.energyMatrix.Energy_2[0] - self.evList[0].realizedDemand
            self.q[0] = remainingEnergy
                
        
        
        return (self.solution_policy, self.q)
        
   
    def RunOptimalPolicy_fromScratch(self):
        
        remainingEnergy = self.uav.capacity
        x = 10000
        
        for j in range(len(self.evList) - 1):
            
            # Compute constant functions, H2 and H3
            value2 = self.H2_policy(j, self.energyMatrix.Energy_3[j])
            value3 = self.H3_policy(j, self.energyMatrix.Energy_3[j])
            
            
            # Compute remaining energy for initial (0th) EV
            if j == 0:
                remainingEnergy = remainingEnergy - self.energyMatrix.Energy_2[j] - self.evList[j].realizedDemand
                self.q[j] = remainingEnergy
            
            
            
            # Fig. 4
            if value3 < value2:
                # find h_j
                h_j = 9999
                for q in reversed(range(int(remainingEnergy) + 1)):
                    value1 = self.H1_policy(j, q)    
                    if value1 <= value3:
                        h_j = q
                    else:
                        break
                    
                if remainingEnergy < h_j:
                    x = 2
                    self.solution_policy.append(x)
                else:
                    x = 0
                    self.solution_policy.append(x)
                
                
            
            # Fig. 5
            elif value3 >= value2:
                # find h_j
                h_j = 9999
                
                for q in reversed(range(int(remainingEnergy) + 1)):
                    value1 = self.H1_policy(j, q)    
                    if value1 <= value2:
                        h_j = q
                    else:
                        break
                    
                    
                if remainingEnergy < self.energyMatrix.Energy_3[j]:
                    x = 2
                    self.solution_policy.append(x)
                elif remainingEnergy < h_j:
                    x = 1
                    self.solution_policy.append(x)
                else:
                    x = 0
                    self.solution_policy.append(x)
            
            
            # remaining energy update
            if x == 0:
                if remainingEnergy >= self.energyMatrix.Energy_4[j, j+1] + self.evList[j+1].realizedDemand:
                    remainingEnergy = remainingEnergy - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].realizedDemand
                    self.q[j+1] = remainingEnergy
                else:
                    remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].realizedDemand
                    self.q[j+1] = remainingEnergy
                
            elif x == 1:
                remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].realizedDemand
                self.q[j+1] = remainingEnergy
            
            elif x == 2:
                remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].realizedDemand
                self.q[j+1] = remainingEnergy
            
            
            
            
          
        # last ev
        if remainingEnergy < self.energyMatrix.Energy_3[len(self.evList) - 1]:
            x = 2
        else:
            x = 0
        self.solution_policy.append(x)
        
        return (self.solution_policy, self.q)
    
    
    
    def RunOptimalPolicy_New(self):
        
        # Solve DP using threshold theorem
        x_j_q = [[9999] * (self.uav.capacity + 1) for _ in range(len(self.evList))]
        
        
        for j in reversed(range(len(self.evList))):
            
            # boundary condition
            if (j == len(self.evList) - 1):
                
                for q in range(self.uav.capacity + 1):
                    if q < self.energyMatrix.Energy_3[len(self.evList) - 1]:
                        x_j_q[j][q] = 2
                    else:
                        x_j_q[j][q] = 0
            
            # f_j(q)
            else:   
                # Compute constant functions, H2 and H3
                value2 = self.H2_policy(j, self.energyMatrix.Energy_3[j])
                value3 = self.H3_policy(j, self.energyMatrix.Energy_3[j])
                             
                # Fig. 4
                if value3 < value2:
                    # find h_j
                    h_j = 9999
                    for q in reversed(range(int(self.uav.capacity) + 1)):
                        value1 = self.H1_policy(j, q)    
                        if value1 <= value3:
                            h_j = q
                            x_j_q[j][q] = 0
                        else:
                            x_j_q[j][q] = 2
                        

                
                # Fig. 5
                elif value3 >= value2:
                    # find h_j
                    h_j = 9999
                    
                    for q in reversed(range(int(self.uav.capacity) + 1)):
                        value1 = self.H1_policy(j, q)    
                        if value1 <= value2:
                            h_j = q
                            x_j_q[j][q] = 0
                        else:
                            if self.energyMatrix.Energy_3[j] <= q and q < h_j:
                                x_j_q[j][q] = 1
                            elif q < self.energyMatrix.Energy_3[j]:
                                x_j_q[j][q] = 2
                            
        
        # Find solution
        remainingEnergy = self.uav.capacity
        
        for j in range(len(self.evList) - 1):
        
            # Compute remaining energy for initial (0th) EV
            if j == 0:
                remainingEnergy = remainingEnergy - self.energyMatrix.Energy_2[j] - self.evList[j].realizedDemand
            
            
            self.q[j] = remainingEnergy
            self.solution_policy.append(x_j_q[j][int(remainingEnergy)])
            
            
            # remaining energy update
            if self.solution_policy[-1] == 0:
                if remainingEnergy >= self.energyMatrix.Energy_4[j, j+1] + self.evList[j+1].realizedDemand:
                    remainingEnergy = remainingEnergy - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].realizedDemand
                    
                else:
                    remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].realizedDemand
                    
                
            elif self.solution_policy[-1] == 1:
                remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].realizedDemand
                
            
            elif self.solution_policy[-1] == 2:
                remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].realizedDemand
                
        
        # last EV
        self.q[len(self.evList) - 1] = remainingEnergy
        self.solution_policy.append(x_j_q[len(self.evList) - 1][int(remainingEnergy)])
        
        
        
        return (self.solution_policy, self.q)
    
    
    
    
      
      
      
      
    def DPVerification(self, solution):
        remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_2[0] - self.evList[0].realizedDemand
        
        flag = True
        for j in range(len(solution) - 1):
            if (solution[j] == 0):
                if self.energyMatrix.Energy_4[j, j+1] + self.evList[j+1].realizedDemand <= remainingEnergy:
                    remainingEnergy = remainingEnergy - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].realizedDemand
                    
                else:
                    if(remainingEnergy - self.energyMatrix.Energy_4[j, j+1] - self.energyMatrix.Energy_2[j+1] < 0):
                        flag = False
                        break
                    remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].realizedDemand
                
            elif (solution[j] == 1):
                if(remainingEnergy - self.energyMatrix.Energy_3[j] < 0):
                    flag = False
                    break
                remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].realizedDemand
                
            elif (solution[j] == 2):
                remainingEnergy = self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].realizedDemand
                
            if(remainingEnergy < 0):
                flag = False
                break
        
        if(flag):    
            if(solution[len(solution) - 1] == 0):
                if(remainingEnergy - self.energyMatrix.Energy_3[len(solution) - 1] < 0):
                    flag = False
                
                
        return flag
    
    
    
    
    
    def RunDP(self):
        remainingElectricity = self.uav.capacity - self.energyMatrix.Energy_2[0] - self.evList[0].realizedDemand
        
        for evIndex in range(len(self.evList)):
            if (self.f_array[evIndex, int(remainingElectricity)] == 0):
                self.f(evIndex, int(remainingElectricity))
                
            
            # solution save    
            x = self.x_array[evIndex, int(remainingElectricity)]      
            self.solution.append(x)

            # remaining electricity update
            if(evIndex == len(self.evList) - 1):
                if(self.x_array[evIndex, int(remainingElectricity)] == 0):
                    
                    remainingElectricity = remainingElectricity - self.energyMatrix.Energy_3[evIndex]
                    
                    
                elif(self.x_array[evIndex, int(remainingElectricity)] == 2):
                    remainingElectricity = self.uav.capacity - self.energyMatrix.Energy_3[evIndex]
                    
                
                
            else:
                if(self.x_array[evIndex, int(remainingElectricity)] == 0):
                    if remainingElectricity >= self.energyMatrix.Energy_4[evIndex, evIndex+1] + self.evList[evIndex+1].realizedDemand: 
                        remainingElectricity = remainingElectricity - self.energyMatrix.Energy_4[evIndex, evIndex+1] - self.evList[evIndex+1].realizedDemand
                    else:
                        
                        remainingElectricity = self.uav.capacity - self.energyMatrix.Energy_2[evIndex+1] - self.evList[evIndex+1].realizedDemand
                        
                        
                    
                elif(self.x_array[evIndex, int(remainingElectricity)] == 1):  
                    remainingElectricity = self.uav.capacity - self.energyMatrix.Energy_2[evIndex+1] - self.evList[evIndex+1].realizedDemand
                    
                    
                elif(self.x_array[evIndex, int(remainingElectricity)] == 2):
                    remainingElectricity = self.uav.capacity - self.energyMatrix.Energy_4[evIndex, evIndex+1] - self.evList[evIndex+1].realizedDemand
        
        
        
            
        return self.solution
    
    
    
    
    
        
    def f(self, j, q):
        # Boundary condition
        if j == (len(self.evList) - 1):
            value1 = self.costMatrix.Cost_3[j] + (self.M * (1 if self.energyMatrix.Energy_3[j] > q else 0))
            value2 = self.uav.chargeFee + self.costMatrix.Cost_3[j]
            
            if value1 <= value2:
                self.f_array[j, int(q)] = value1
                self.x_array[j, int(q)] = 0
                
            else:
                self.f_array[j, int(q)] = value2
                self.x_array[j, int(q)] = 2
                
                
        # Eq. (1)    
        else:
            sum1 = self.H1(j, q)
            sum2 = self.H2(j, q)
            sum3 = self.H3(j, q)
            
            self.f_array[j, int(q)] = min(sum1, sum2, sum3)
            
            if self.f_array[j, int(q)] == sum1:
                self.x_array[j, int(q)] = 0
                
            elif self.f_array[j, int(q)] == sum2:
                self.x_array[j, int(q)] = 1
                
            elif self.f_array[j, int(q)] == sum3:
                self.x_array[j, int(q)] = 2
                
            else:
                ctypes.windll.user32.MessageBoxW(0, "Something goes wrong in DP", "Error", 1)
                quit()
    
    
    def f_policy(self, j, q):
        # Boundary condition
        if j == (len(self.evList) - 1):
            value1 = self.costMatrix.Cost_3[j] + (self.M * (1 if self.energyMatrix.Energy_3[j] > q else 0))
            value2 = self.uav.chargeFee + self.costMatrix.Cost_3[j]
            
            if value1 <= value2:
                self.f_array_policy[j, int(q)] = value1
                self.x_array_policy[j, int(q)] = 0
                
            else:
                self.f_array_policy[j, int(q)] = value2
                self.x_array_policy[j, int(q)] = 2
                
                
        # Eq. (1)    
        else:
            sum1 = self.H1_policy(j, q)
            sum2 = self.H2_policy(j, q)
            sum3 = self.H3_policy(j, q)
            
            self.f_array_policy[j, int(q)] = min(sum1, sum2, sum3)
            
            if self.f_array_policy[j, int(q)] == sum1:
                self.x_array_policy[j, int(q)] = 0
                
            elif self.f_array_policy[j, int(q)] == sum2:
                self.x_array_policy[j, int(q)] = 1
                
            elif self.f_array_policy[j, int(q)] == sum3:
                self.x_array_policy[j, int(q)] = 2
                
            else:
                ctypes.windll.user32.MessageBoxW(0, "Something goes wrong in DP", "Error", 1)
                quit()
         
         
                
    def H1_policy(self, j, q):
        # Eq. (1.1)
        sum1 = 0.0
        for k in range(len(self.evList[j+1].demandProb)):
            if q >= self.energyMatrix.Energy_4[j, j+1] + self.evList[j+1].demandProb[k][0]:
                if(self.f_array_policy[j+1, int(q - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].demandProb[k][0])] == 0):
                    self.f_policy(j+1, q - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].demandProb[k][0])
                    
                sum1 = sum1 + (self.f_array_policy[j+1, int(q - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].demandProb[k][0])] * self.evList[j+1].demandProb[k][1]) 
                    
            if q < self.energyMatrix.Energy_4[j, j+1] + self.evList[j+1].demandProb[k][0]:
                if(self.f_array_policy[j + 1, int(self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].demandProb[k][0])] == 0):
                    self.f_policy(j + 1, self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].demandProb[k][0])
                
                sum1 = sum1 + (((2*self.costMatrix.Cost_2[j+1]) + self.uav.routeFailureCost + self.f_array_policy[j + 1, int(self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].demandProb[k][0])]) * self.evList[j+1].demandProb[k][1])
                    
        sum1 = sum1 + (self.M * 1 if q < self.energyMatrix.Energy_4[j, j+1] + self.energyMatrix.Energy_2[j+1] else 0)
        sum1 = sum1 + self.costMatrix.Cost_4[j, j+1]  
        
        return sum1
    
    
    def H2_policy(self, j, q):
        # Eq. (1.2)
        sum2 = 0.0
        for k in range(len(self.evList[j+1].demandProb)):
            if(self.f_array_policy[j+1, int(self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].demandProb[k][0])] == 0):
                self.f_policy(j+1, self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].demandProb[k][0])
            
            sum2 = sum2 + (self.f_array_policy[j+1, int(self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].demandProb[k][0])] * self.evList[j+1].demandProb[k][1])
                
        sum2 = sum2 + self.costMatrix.Cost_3[j]
        sum2 = sum2 + self.costMatrix.Cost_2[j+1]
        sum2 = sum2 + (self.M * (1 if self.energyMatrix.Energy_3[j] > q else 0))
            
        return sum2
    
    
    def H3_policy(self, j, q):
        # Eq. (1.3)  
        sum3 = 0.0
        for k in range(len(self.evList[j+1].demandProb)):
            if(self.f_array_policy[j+1, int(self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].demandProb[k][0])] == 0):
                self.f_policy(j+1, self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].demandProb[k][0])
            
            sum3 = sum3 + (self.f_array_policy[j+1, int(self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].demandProb[k][0])] * self.evList[j+1].demandProb[k][1])
                
        sum3 = sum3 + self.costMatrix.Cost_4[j, j+1]
        sum3 = sum3 + self.uav.chargeFee
        
        return sum3
    
    
    
                
    def H1(self, j, q):
        # Eq. (1.1)
        sum1 = 0.0
        for k in range(len(self.evList[j+1].demandProb)):
            if q >= self.energyMatrix.Energy_4[j, j+1] + self.evList[j+1].demandProb[k][0]:
                if(self.f_array[j+1, int(q - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].demandProb[k][0])] == 0):
                    self.f(j+1, q - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].demandProb[k][0])
                    
                sum1 = sum1 + (self.f_array[j+1, int(q - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].demandProb[k][0])] * self.evList[j+1].demandProb[k][1]) 
                    
            if q < self.energyMatrix.Energy_4[j, j+1] + self.evList[j+1].demandProb[k][0]:
                if(self.f_array[j + 1, int(self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].demandProb[k][0])] == 0):
                    self.f(j + 1, self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].demandProb[k][0])
                
                sum1 = sum1 + (((2*self.costMatrix.Cost_2[j+1]) + self.uav.routeFailureCost + self.f_array[j + 1, int(self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].demandProb[k][0])]) * self.evList[j+1].demandProb[k][1])
        
      
        sum1 = sum1 + (self.M * 1 if q < (self.energyMatrix.Energy_4[j, j+1] + self.energyMatrix.Energy_2[j+1]) else 0)
        sum1 = sum1 + self.costMatrix.Cost_4[j, j+1]  
        
        return sum1
    
    
    def H2(self, j, q):
        # Eq. (1.2)
        sum2 = 0.0
        for k in range(len(self.evList[j+1].demandProb)):
            if(self.f_array[j+1, int(self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].demandProb[k][0])] == 0):
                self.f(j+1, self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].demandProb[k][0])
            
            sum2 = sum2 + (self.f_array[j+1, int(self.uav.capacity - self.energyMatrix.Energy_2[j+1] - self.evList[j+1].demandProb[k][0])] * self.evList[j+1].demandProb[k][1])
        
       
        
        sum2 = sum2 + self.costMatrix.Cost_3[j]
        sum2 = sum2 + self.costMatrix.Cost_2[j+1]
        sum2 = sum2 + (self.M * (1 if self.energyMatrix.Energy_3[j] > q else 0))
            
        return sum2
    
    
    def H3(self, j, q):
        # Eq. (1.3)  
        sum3 = 0.0
        for k in range(len(self.evList[j+1].demandProb)):
            if(self.f_array[j+1, int(self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].demandProb[k][0])] == 0):
                self.f(j+1, self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].demandProb[k][0])
            
            sum3 = sum3 + (self.f_array[j+1, int(self.uav.capacity - self.energyMatrix.Energy_4[j, j+1] - self.evList[j+1].demandProb[k][0])] * self.evList[j+1].demandProb[k][1])
                
        sum3 = sum3 + self.costMatrix.Cost_4[j, j+1]
        sum3 = sum3 + self.uav.chargeFee
        
        return sum3