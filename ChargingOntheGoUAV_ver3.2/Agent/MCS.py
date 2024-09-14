from Node.Node import Node
from Agent.Schedule import Schedule
import ctypes
import numpy as np

class MCS():
    def __init__(self, capacity, state, chargingRate, startTime, evList, unitDiscrete):
        self.capacity = state.Discretized(capacity)   # discretized capacity
        self.remainingEnergy = self.capacity
        self.chargingRate = chargingRate    # unit: kW
        self.scheduleList = []
        self.startTime = startTime  # unit: second
        self.evList = evList
        # self.remainingEnergy = []   # unit: kWh
        self.odMatrix = None
        self.energyTimeMatrix = None
        self.solution = None
        self.objValue = 0
        self.unitDiscrete = unitDiscrete
      
        
    def GenerateSchedule(self):
        
        for iter, ev in enumerate(self.evList):
            self.scheduleList.append(Schedule())
            self.scheduleList[-1].evIndex = ev.index
            
            if iter == 0:
                # rendezvous location 도착시각 계산 (depot 에서 옴)
                self.scheduleList[-1].rendezvous_arrivalTime = self.startTime + self.energyTimeMatrix.Time_1[ev.index]
            
            else:
                # rendezvous location 도착시각 계산 (이전 고객에서 옴)
                travelTime = self.energyTimeMatrix.Time_2[self.evList[iter - 1].index, ev.index]
                self.scheduleList[-1].rendezvous_arrivalTime = self.scheduleList[-2].rendezvous_departureTime + travelTime
                
            
            # rendezvous 출발시각 계산
            chargingTime = ((ev.realizedDemand * self.unitDiscrete) / self.chargingRate) * 3600.0   # EV를 충전하는데 소요되는 시간 (sec)
                
            self.scheduleList[-1].rendezvous_departureTime = self.scheduleList[-1].rendezvous_arrivalTime + chargingTime
            
            
    def CheckCapacity(self):
        totalUsedEnergy = 0.0
        for iter, ev in enumerate(self.evList):
            if iter == 0:
                totalUsedEnergy += self.energyTimeMatrix.Energy_1[ev.index]
            else:
                totalUsedEnergy += self.energyTimeMatrix.Energy_2[self.evList[iter - 1].index, ev.index]
            
            totalUsedEnergy += ev.realizedDemand
        totalUsedEnergy += self.energyTimeMatrix.Energy_1[self.evList[-1].index]
        
        if totalUsedEnergy > self.capacity:
            ctypes.windll.user32.MessageBoxW(0, "capacity exceeds!", "title", 16)    
        
        
    # Generate depot
    def setDepot(self, x, y):    
        self.depot = Node(0, x, y)
        
        
    # Update remaining energy
    def UpdateRemainingEnergy(self, updatedRemainingEnergy):
        self.remainingEnergy = updatedRemainingEnergy