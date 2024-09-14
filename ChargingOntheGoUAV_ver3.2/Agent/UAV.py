from Node.Node import Node
from Agent.Schedule import Schedule
import numpy as np

class UAV():
    def __init__(self, routeFailureCost, chargeFee, unitFlightCost, energyConsumptionRate, capacity, state, numEV, chargingRate, startTime, uavSpeed, evList, unitDiscrete):
        self.routeFailureCost = routeFailureCost
        self.chargeFee = chargeFee
        self.unitFlightCost = unitFlightCost
        self.energyConsumptionRate = energyConsumptionRate
        self.capacity = state.Discretized(capacity)   # discretized capacity
        self.remainingEnergy = self.capacity
        self.h = np.zeros(numEV)
        self.chargingRate = chargingRate    # unit: kW
        self.scheduleList = []
        self.scheduleList_MIP = []
        self.startTime = startTime  # unit: second
        self.uavSpeed = uavSpeed / 1000.0   # unit: km/s
        self.evList = evList
        self.remainingEnergyList = []   # unit: kWh
        self.odMatrix = None
        self.energyMatrix = None
        self.costMatrix = None
        self.dp = None
        self.solution_DP = None
        self.solution_policy = None
        self.objValue_DP = 0
        self.objValue_policy = 0
        self.CPUTime_DP = 0
        self.CPUTime_policy = 0
        self.unitDiscrete = unitDiscrete
        self.feasible_DP = None
        self.objValue_MIP = None
        self.CPUTime_MIP = None
        self.feasible_MIP = None
        self.x1_MIP = None
        self.x2_MIP = None
        self.y_MIP = None
        self.z_MIP = None
        
    
    
    def GenerateSchedule_MIP(self):
        solution = []
        for iter in range(len(self.x1_MIP)):
            if round(self.x1_MIP[iter], 0) == 1:
                solution.append(0)
            elif round(self.x2_MIP[iter], 0) == 1:
                solution.append(3)
            elif round(self.y_MIP[iter], 0) == 1:
                solution.append(1)
            elif round(self.z_MIP[iter], 0) == 1:
                solution.append(2)
        
            
        # 어찌됐든, solution 순서대로 EV를 수행하는 거임
        for iter, ev in enumerate(self.evList):
            self.scheduleList_MIP.append(Schedule())
            self.scheduleList_MIP[-1].evIndex = ev.index
            
            if iter == 0:
                # rendezvous location 도착시각 계산
                travelDistance = self.odMatrix.OD_2[ev.index]    # unit: km
                travelTime = travelDistance / self.uavSpeed # unit: sec.
                self.scheduleList_MIP[-1].rendezvous_arrivalTime = self.startTime + travelTime
            
            else:
                # rendezvous location 도착시각 계산
                if solution[iter - 1] == 0:    # 이전 고객에서 옴
                    travelTime = self.odMatrix.OD_4[self.evList[iter - 1].index, self.evList[iter].index] / self.uavSpeed
                    self.scheduleList_MIP[-1].rendezvous_arrivalTime = self.scheduleList_MIP[-2].destination_departureTime + travelTime
                
                elif solution[iter - 1] == 1:  # depot에서 옴
                    travelTime = self.odMatrix.OD_2[self.evList[iter].index] / self.uavSpeed
                    self.scheduleList_MIP[-1].rendezvous_arrivalTime = self.scheduleList_MIP[-2].depot_departureTime + travelTime
                    
                elif solution[iter - 1] == 2:  # 이전 고객에서 옴
                    travelTime = self.odMatrix.OD_4[self.evList[iter - 1].index, self.evList[iter].index] / self.uavSpeed
                    self.scheduleList_MIP[-1].rendezvous_arrivalTime = self.scheduleList_MIP[-2].destination_departureTime + travelTime
                
                elif solution[iter - 1] == 3: # rendezvous location 도착했다가, 다시 depot 갔다가, depot에서 충전했다가, 다시 rendezvous location에 도착함
                    travelTime = self.odMatrix.OD_4[self.evList[iter - 1].index, self.evList[iter].index] / self.uavSpeed   # 이전 고객에서 옴
                    travelTime += self.odMatrix.OD_2[self.evList[iter].index] / self.uavSpeed   # depot로 복귀
                    remainingEnergy = self.remainingEnergyList[iter - 1] - self.energyMatrix.Energy_4[self.evList[iter - 1].index, self.evList[iter].index] - self.energyMatrix.Energy_2[self.evList[iter].index]  # depot 복귀후 남은 energy
                    chargingTime = (((self.capacity - remainingEnergy) * self.unitDiscrete) / self.chargingRate) * 3600.0 # 충전 소요 시간 (sec)
                    travelTime += self.odMatrix.OD_2[self.evList[iter].index] / self.uavSpeed   # rendezvous location에 도착
                    self.scheduleList_MIP[-1].rendezvous_arrivalTime = self.scheduleList_MIP[-2].destination_departureTime + travelTime + chargingTime
            
            
            # destination 도착시각 계산
            travelTime = 0.0
            for iter2, distance in enumerate(ev.distances):
                travelTime += (distance / ev.speeds[iter2]) * 3600.0    # unit: sec.
            self.scheduleList_MIP[-1].destination_arrivalTime = self.scheduleList_MIP[-1].rendezvous_arrivalTime + travelTime
            
            
            # destination 출발시각 계산
            if solution[iter] == 0:    # 바로 다음 고객으로 이동
                self.scheduleList_MIP[-1].destination_departureTime = self.scheduleList_MIP[-1].destination_arrivalTime
            elif solution[iter] == 1:  # depot들렸다가 다음 고객으로 이동
                self.scheduleList_MIP[-1].destination_departureTime = self.scheduleList_MIP[-1].destination_arrivalTime
            elif solution[iter] == 2:  # 현재 위치에서 충전했다가 다음 고객으로 이동
                chargingTime = (((self.capacity - self.remainingEnergyList[iter]) * self.unitDiscrete) / self.chargingRate) * 3600.0 # 충전 소요 시간 (sec)
                self.scheduleList_MIP[-1].destination_departureTime = self.scheduleList_MIP[-1].destination_arrivalTime + chargingTime
            elif solution[iter] == 3:   # 바로 다음 고객으로 이동 (rendezvous location 도착시각 계산에서 depot 다녀오는거 계산됨)
                self.scheduleList_MIP[-1].destination_departureTime = self.scheduleList_MIP[-1].destination_arrivalTime
            
            
            # depot 도착시각 & 출발시각 계산
            if solution[iter] == 0:    # 바로 다음 고객으로 이동
                self.scheduleList_MIP[-1].depot_arrivalTime = 99999
                self.scheduleList_MIP[-1].depot_departureTime = 99999
                
            elif solution[iter] == 1:  # depot들렸다가 다음 고객으로 이동
                travelTime = self.odMatrix.OD_3[ev.index] / self.uavSpeed
                self.scheduleList_MIP[-1].depot_arrivalTime = self.scheduleList_MIP[-1].destination_departureTime + travelTime
                
                
                remainingEnergy = self.remainingEnergyList[iter] - self.energyMatrix.Energy_3[ev.index]
                chargingTime = (((self.capacity - remainingEnergy) * self.unitDiscrete) / self.chargingRate) * 3600.0 # 충전 소요 시간 (sec)
                
                self.scheduleList_MIP[-1].depot_departureTime = self.scheduleList_MIP[-1].depot_arrivalTime + chargingTime
                
            elif solution[iter] == 2:  # 현재 위치에서 충전했다가 다음 고객으로 이동
                self.scheduleList_MIP[-1].depot_arrivalTime = 99999
                self.scheduleList_MIP[-1].depot_departureTime = 99999
            
            elif solution[iter] == 3:   # 바로 다음 고객으로 이동 (rendezvous location 도착시각 계산에서 depot 다녀오는거 계산됨)
                self.scheduleList_MIP[-1].depot_arrivalTime = 99999
                self.scheduleList_MIP[-1].depot_departureTime = 99999
        
    
    
        
        
    def GenerateSchedule(self):
        if self.solution_policy != None:
            solution = self.solution_policy
        else:
            solution = self.solution_DP
            
            
        # 어찌됐든, solution 순서대로 EV를 수행하는 거임
        for iter, ev in enumerate(self.evList):
            self.scheduleList.append(Schedule())
            self.scheduleList[-1].evIndex = ev.index
            
            if iter == 0:
                # rendezvous location 도착시각 계산
                travelDistance = self.odMatrix.OD_2[ev.index]    # unit: km
                travelTime = travelDistance / self.uavSpeed # unit: sec.
                self.scheduleList[-1].rendezvous_arrivalTime = self.startTime + travelTime
            
            else:
                # rendezvous location 도착시각 계산
                if solution[iter - 1] == 0:    # 이전 고객에서 옴
                    travelTime = self.odMatrix.OD_4[self.evList[iter - 1].index, self.evList[iter].index] / self.uavSpeed
                    self.scheduleList[-1].rendezvous_arrivalTime = self.scheduleList[-2].destination_departureTime + travelTime
                
                elif solution[iter - 1] == 1:  # depot에서 옴
                    travelTime = self.odMatrix.OD_2[self.evList[iter].index] / self.uavSpeed
                    self.scheduleList[-1].rendezvous_arrivalTime = self.scheduleList[-2].depot_departureTime + travelTime
                    
                elif solution[iter - 1] == 2:  # 이전 고객에서 옴
                    travelTime = self.odMatrix.OD_4[self.evList[iter - 1].index, self.evList[iter].index] / self.uavSpeed
                    self.scheduleList[-1].rendezvous_arrivalTime = self.scheduleList[-2].destination_departureTime + travelTime
            
            
            
            # destination 도착시각 계산
            travelTime = 0.0
            for iter2, distance in enumerate(ev.distances):
                travelTime += (distance / ev.speeds[iter2]) * 3600.0    # unit: sec.
            self.scheduleList[-1].destination_arrivalTime = self.scheduleList[-1].rendezvous_arrivalTime + travelTime
            
            
            # destination 출발시각 계산
            if solution[iter] == 0:    # 바로 다음 고객으로 이동
                self.scheduleList[-1].destination_departureTime = self.scheduleList[-1].destination_arrivalTime
            elif solution[iter] == 1:  # depot들렸다가 다음 고객으로 이동
                self.scheduleList[-1].destination_departureTime = self.scheduleList[-1].destination_arrivalTime
            elif solution[iter] == 2:  # 현재 위치에서 충전했다가 다음 고객으로 이동
                chargingTime = (((self.capacity - self.remainingEnergyList[iter]) * self.unitDiscrete) / self.chargingRate) * 3600.0 # 충전 소요 시간 (sec)
                self.scheduleList[-1].destination_departureTime = self.scheduleList[-1].destination_arrivalTime + chargingTime
            
            
            # depot 도착시각 & 출발시각 계산
            if solution[iter] == 0:    # 바로 다음 고객으로 이동
                self.scheduleList[-1].depot_arrivalTime = 99999
                self.scheduleList[-1].depot_departureTime = 99999
                
            elif solution[iter] == 1:  # depot들렸다가 다음 고객으로 이동
                travelTime = self.odMatrix.OD_3[ev.index] / self.uavSpeed
                self.scheduleList[-1].depot_arrivalTime = self.scheduleList[-1].destination_departureTime + travelTime
                
                
                remainingEnergy = self.remainingEnergyList[iter] - self.energyMatrix.Energy_3[ev.index]
                chargingTime = (((self.capacity - remainingEnergy) * self.unitDiscrete) / self.chargingRate) * 3600.0 # 충전 소요 시간 (sec)
                
                
                
                self.scheduleList[-1].depot_departureTime = self.scheduleList[-1].depot_arrivalTime + chargingTime
                
            elif solution[iter] == 2:  # 현재 위치에서 충전했다가 다음 고객으로 이동
                self.scheduleList[-1].depot_arrivalTime = 99999
                self.scheduleList[-1].depot_departureTime = 99999
            
            
        
        
        
    # Generate depot
    def setDepot(self, x, y):    
        self.depot = Node(0, x, y)
        
        
    # Update remaining energy
    def UpdateRemainingEnergy(self, updatedRemainingEnergy):
        self.remainingEnergy = updatedRemainingEnergy