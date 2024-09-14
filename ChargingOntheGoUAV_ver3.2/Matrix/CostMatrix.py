import numpy as np


class CostMatrix():
    def __init__(self, unitFlightCost, energyMatrix, evList):

        
        # (0, j+) : (depot node, rendezvous node of all customers)
        # n x 1 matrix (column)
        self.Cost_2 = np.empty([len(evList)])
        self.Cost_2.fill(100000000.0)
        
        # (j-, 0) : (destination node  of all customers, depot node)
        self.Cost_3 = np.empty([len(evList)])
        self.Cost_3.fill(100000000.0)
        
        # (j-, (j+1)+)) : (destination node of all customers, rendezvous node of all customers)
        self.Cost_4 = np.empty([len(evList), len(evList)])
        self.Cost_4.fill(100000000.0)
        
        

        
        # Cost_2 setting
        for i in range(len(evList)):
            self.Cost_2[evList[i].index] = unitFlightCost * energyMatrix.Energy_2[evList[i].index]
            
            
        # Cost_3 setting
        for i in range(len(evList)):
            self.Cost_3[evList[i].index] = unitFlightCost * energyMatrix.Energy_3[evList[i].index]
            
            
        # Cost_4 setting
        for i in range(len(evList)):
            for j in range(len(evList)):
                if i != j:
                    self.Cost_4[evList[i].index, evList[j].index] = unitFlightCost * energyMatrix.Energy_4[evList[i].index, evList[j].index]