import numpy as np
import random
from State.State import State

class EnergyMatrix():
    def __init__(self, energyConsumptionRate, odMatrix, evList, state):
        
       
        # (0, j+) : (depot node, rendezvous node of all customers)
        # n x 1 matrix (column)
        self.Energy_2 = np.empty([len(evList)])
        self.Energy_2.fill(100000000.0)
        
        # (j-, 0) : (destination node  of all customers, depot node)
        self.Energy_3 = np.empty([len(evList)])
        self.Energy_3.fill(100000000.0)
        
        # (j-, (j+1)+)) : (destination node of all customers, rendezvous node of all customers)
        self.Energy_4 = np.empty([len(evList), len(evList)])
        self.Energy_4.fill(100000000.0)
        
        
       
        
        # Energy_2 setting
        for i in range(len(evList)):
            self.Energy_2[evList[i].index] = state.Discretized(energyConsumptionRate * odMatrix.OD_2[evList[i].index]) 
            
        # Energy_3 setting
        for i in range(len(evList)):
            self.Energy_3[evList[i].index] = state.Discretized(energyConsumptionRate * odMatrix.OD_3[evList[i].index]) 
            
        # Energy_4 setting
        for i in range(len(evList)):
            for j in range(len(evList)):
                if i != j:
                    self.Energy_4[evList[i].index, evList[j].index] = state.Discretized(energyConsumptionRate * odMatrix.OD_4[evList[i].index, evList[j].index]) 
                    
                    
class EnergyTimeMatrix_MCS():
    def __init__(self, odMatrix, evList, state, seed, UnitDistPowerConsumption_mean0, UnitDistPowerConsumption_mean1, 
                 UnitDistPowerConsumption_mean2, UnitDistPowerConsumption_mean3, speed0, speed1, speed2, speed3, arm_Tri):
        rndEVDemandGenerator = random.Random(seed) 
       
        # (0, j+) : (depot node, rendezvous node of all customers)
        # n x 1 matrix (column)
        self.Energy_1 = np.empty([len(evList)])
        self.Energy_1.fill(100000000.0)
        
        self.Time_1 = np.empty([len(evList)])
        self.Time_1.fill(100000000.0)
        
        
        
        # (j+, (j+1)+)) : (rendezvous node of a customer, rendezvous node of the following customer)
        self.Energy_2 = np.empty([len(evList), len(evList)])
        self.Energy_2.fill(100000000.0)
        
        self.Time_2 = np.empty([len(evList), len(evList)])
        self.Time_2.fill(100000000.0)
        
        
        
        # MCS의 이동시 소요되는 에너지 계산 하는 거임 (EV 충전량 아님)
        # Energy_1 setting
        for i in range(len(evList)):
            # road type은 랜덤하게 선택 후 랜덤하게 배분
            speeds = []
            unitPowerConsumptionMeans = []
            for j in range(4):
                speedType = rndEVDemandGenerator.randint(0, 3)
                if speedType == 0:
                    speeds.append(speed0)
                    unitPowerConsumptionMeans.append(UnitDistPowerConsumption_mean0)
                elif speedType == 1:
                    speeds.append(speed1)
                    unitPowerConsumptionMeans.append(UnitDistPowerConsumption_mean1)
                elif speedType == 2:
                    speeds.append(speed2)
                    unitPowerConsumptionMeans.append(UnitDistPowerConsumption_mean2)
                elif speedType == 3:
                    speeds.append(speed3)
                    unitPowerConsumptionMeans.append(UnitDistPowerConsumption_mean3)
                    
                    
            distances = []
            totalDistance = round(odMatrix.OD_1[evList[i].index] * 1000000, 0)
            for j in range(4):
                if j == 3:
                    distance = round(totalDistance / 1000000, 3)
                    distances.append(distance)
                else:
                    distance = rndEVDemandGenerator.randrange(totalDistance)
                    distance = round(distance, 0)
                    totalDistance = totalDistance - distance
                    
                    distance = round(distance / 1000000, 3)
                    distances.append(distance)
            
            
            travelTime = 0.0
            for j in range(len(distances)):
                travelTime += distances[j] / speeds[j] * 3600
            self.Time_1[evList[i].index] = travelTime
            
            
            
            # Discretized power consumption (= electricity demand) center
            totalPowerConsumption = 0.0
            for j in range(len(distances)):
                totalPowerConsumption += distances[j] * unitPowerConsumptionMeans[j]
            discretizedElectricityDemandCenter = State().Discretized(totalPowerConsumption)
            
            
                    
            # realized energy requirement 계산해야됨
            # Make cumulative probabilities
            
            demandProb = []
            self.setDemandProb(demandProb, discretizedElectricityDemandCenter, arm_Tri)
            
            cumProbabilities = []
            sumProb = 0.0
            for j in range(len(demandProb)):
                sumProb = sumProb + demandProb[j][1]
                cumProbabilities.append((demandProb[j][0], sumProb))
            
            
            # Set realized demand
            randomNumber = rndEVDemandGenerator.random()
            value = -9999
            if 0.0 <= randomNumber and randomNumber <= cumProbabilities[0][1]:
                value = cumProbabilities[0][0]
            
            if value == -9999:
                for j in range(len(cumProbabilities) - 1):
                    if cumProbabilities[j][1] < randomNumber and randomNumber <= cumProbabilities[j+1][1]:
                        value = cumProbabilities[j+1][0]
                        break
            
            if value == -9999:
                value = cumProbabilities[len(cumProbabilities) - 1][0]
            
            self.Energy_1[evList[i].index] = value
            
        
        # Energy_2 setting
        for i in range(len(evList)):
            for j in range(len(evList)):
                if evList[i].index < evList[j].index:
                    
                    # road type은 랜덤하게 선택 후 랜덤하게 배분
                    speeds = []
                    unitPowerConsumptionMeans = []
                    for k in range(4):
                        speedType = rndEVDemandGenerator.randint(0, 3)
                        if speedType == 0:
                            speeds.append(speed0)
                            unitPowerConsumptionMeans.append(UnitDistPowerConsumption_mean0)
                        elif speedType == 1:
                            speeds.append(speed1)
                            unitPowerConsumptionMeans.append(UnitDistPowerConsumption_mean1)
                        elif speedType == 2:
                            speeds.append(speed2)
                            unitPowerConsumptionMeans.append(UnitDistPowerConsumption_mean2)
                        elif speedType == 3:
                            speeds.append(speed3)
                            unitPowerConsumptionMeans.append(UnitDistPowerConsumption_mean3)
                            
                            
                    distances = []
                    totalDistance = round(odMatrix.OD_2[evList[i].index, evList[j].index] * 1000000, 0)
                    for k in range(4):
                        if k == 3:
                            distance = round(totalDistance / 1000000, 3)
                            distances.append(distance)
                        else:
                            distance = rndEVDemandGenerator.randrange(totalDistance)
                            distance = round(distance, 0)
                            totalDistance = totalDistance - distance
                            
                            distance = round(distance / 1000000, 3)
                            distances.append(distance)
                    
                    
                    
                    travelTime = 0.0
                    for k in range(len(distances)):
                        travelTime += distances[k] / speeds[k] * 3600
                    self.Time_2[evList[i].index, evList[j].index] = travelTime
                    
                    
                    
                    # Discretized power consumption (= electricity demand) center
                    totalPowerConsumption = 0.0
                    for k in range(len(distances)):
                        totalPowerConsumption += distances[k] * unitPowerConsumptionMeans[k]
                    discretizedElectricityDemandCenter = State().Discretized(totalPowerConsumption)
                    
                    
                            
                    # realized energy requirement 계산해야됨
                    # Make cumulative probabilities
                    
                    demandProb = []
                    self.setDemandProb(demandProb, discretizedElectricityDemandCenter, arm_Tri)
                    
                    cumProbabilities = []
                    sumProb = 0.0
                    for k in range(len(demandProb)):
                        sumProb = sumProb + demandProb[k][1]
                        cumProbabilities.append((demandProb[k][0], sumProb))
                    
                    
                    # Set realized demand
                    randomNumber = rndEVDemandGenerator.random()
                    value = -9999
                    if 0.0 <= randomNumber and randomNumber <= cumProbabilities[0][1]:
                        value = cumProbabilities[0][0]
                    
                    if value == -9999:
                        for k in range(len(cumProbabilities) - 1):
                            if cumProbabilities[k][1] < randomNumber and randomNumber <= cumProbabilities[k+1][1]:
                                value = cumProbabilities[k+1][0]
                                break
                    
                    if value == -9999:
                        value = cumProbabilities[len(cumProbabilities) - 1][0]
                    
                    self.Energy_2[evList[i].index, evList[j].index] = value
                    
                    
            
       
            
    def setDemandProb(self, probabilities, discretizedElectricityDemandCenter, arm_Tri):
        tempProbabilities = []
        
        for i in range(discretizedElectricityDemandCenter - arm_Tri, discretizedElectricityDemandCenter + arm_Tri + 1):
            if i >= 0:
                tempProbabilities.append((i, (arm_Tri + 1 - abs(i - discretizedElectricityDemandCenter))/((arm_Tri + 1)**2)))
              
            
        sumProbabilities = 0
        for i in range(len(tempProbabilities)):
            sumProbabilities = sumProbabilities + tempProbabilities[i][1]
        
        assignProb = (1 - sumProbabilities) / len(tempProbabilities)
        
                    
        
        for i in range(len(tempProbabilities)):
            probabilities.append((tempProbabilities[i][0], tempProbabilities[i][1] + assignProb))
            
            
            
            
            
            
            
            
            
            
           