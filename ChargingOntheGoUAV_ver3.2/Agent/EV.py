import numpy as np
import random
from scipy.stats import norm
from Node.Node import Node
import ctypes

class EV():
    def __init__(self, index, rendezNode, destinationNode, discretizedElectricityDemandCenter, discretizedElectricityDemandMin, discretizedElectricityDemandMax, seedDemand, speeds, distances, arm_Tri):
        self.index = index
        self.rendezNode = rendezNode
        self.destNode = Node(2, destinationNode.x, destinationNode.y)
        self.speeds = speeds
        self.distances = distances
        self.discretizedElectricityDemandCenter = discretizedElectricityDemandCenter
        self.discretizedElectricityDemandMin = discretizedElectricityDemandMin
        self.discretizedElectricityDemandMax = discretizedElectricityDemandMax
        self.arm_Tri = arm_Tri
       
        
        # values of discrete probability distribution of demand
        self.demandProb = []    # (support, probability)
        self.setDemandProb(self.demandProb)
        
        # expected demand
        self.discretizedExpectedDemand = self.getExpectedDemand() 
        
        
        rndDemandGenerator = random.Random(seedDemand)
        
        # value of a realized discretized demand
        self.realizedDemand = self.getRealizedDemand(rndDemandGenerator.random())

        
        
    
    def getExpectedDemand(self):
        expectedValue = 0.0
        for i in range(len(self.demandProb)):
            expectedValue = expectedValue + (self.demandProb[i][0] * self.demandProb[i][1])
        return expectedValue
    
    
    
    def setDemandProb(self, probabilities):
        '''
        tempProbabilities = []
        
        for i in range(self.discretizedElectricityDemandCenter - self.arm_Tri, self.discretizedElectricityDemandCenter + self.arm_Tri + 1):
            if i > 0:
                tempProbabilities.append((i, 0.0))
                
            
            
        
        assignProb = 1 / len(tempProbabilities)
        
                    
        
        for i in range(len(tempProbabilities)):
            probabilities.append((tempProbabilities[i][0], assignProb))
        '''
        
        
        tempProbabilities = []
        
        for i in range(self.discretizedElectricityDemandCenter - self.arm_Tri, self.discretizedElectricityDemandCenter + self.arm_Tri + 1):
            if i > 0:
                tempProbabilities.append((i, (self.arm_Tri + 1 - abs(i - self.discretizedElectricityDemandCenter))/((self.arm_Tri + 1)**2)))
                
            
            
        sumProbabilities = 0
        for i in range(len(tempProbabilities)):
            sumProbabilities = sumProbabilities + tempProbabilities[i][1]
        
        assignProb = (1 - sumProbabilities) / len(tempProbabilities)
        
                    
        
        for i in range(len(tempProbabilities)):
            probabilities.append((tempProbabilities[i][0], tempProbabilities[i][1] + assignProb))
        
        
        
    def getRealizedDemand(self, randomNumber):
        
        # Make cumulative probabilities
        cumProbabilities = []
        sumProb = 0.0
        for i in range(len(self.demandProb)):
            sumProb = sumProb + self.demandProb[i][1]
            cumProbabilities.append((self.demandProb[i][0], sumProb))
        
        
        # Set realized demand
        value = -9999
        if 0.0 <= randomNumber and randomNumber <= cumProbabilities[0][1]:
            value = cumProbabilities[0][0]
        
        if value == -9999:
            for i in range(len(cumProbabilities) - 1):
                if cumProbabilities[i][1] < randomNumber and randomNumber <= cumProbabilities[i+1][1]:
                    value = cumProbabilities[i+1][0]
                    break
        
        if value == -9999:
            value = cumProbabilities[len(cumProbabilities) - 1][0]
        
        return value