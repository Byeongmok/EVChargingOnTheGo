import numpy as np
import math

class ODMatrix():
    def __init__(self, depot, evList):
        
        # (j+, j-) : (rendezvous node of all customers, destination node of all customers)
        # n x n matrix
        # self.OD_1 = np.empty([len(evList), len(evList)])
        # self.OD_1.fill(100000000.0)
        
        # (0, j+) : (depot node, rendezvous node of all customers)
        # n x 1 matrix (column)
        self.OD_2 = np.empty([len(evList)])
        self.OD_2.fill(100000000.0)
        
        # (j-, 0) : (destination node  of all customers, depot node)
        self.OD_3 = np.empty([len(evList)])
        self.OD_3.fill(100000000.0)
        
        # (j-, (j+1)+)) : (destination node of all customers, rendezvous node of all customers)
        self.OD_4 = np.empty([len(evList), len(evList)])
        self.OD_4.fill(100000000.0)
        
        
        '''
        # OD_1 setting
        for i in range(len(evList)):
            for j in range(len(evList)):
                if i != j:
                    self.OD_1[evList[i].index, evList[j].index] = self.GetKMDistance(evList[i].rendezNode, evList[j].destNode)
        '''
        
        # OD_2 setting
        for i in range(len(evList)):
            self.OD_2[evList[i].index] = self.GetKMDistance(depot, evList[i].rendezNode)
            
        # OD_3 setting
        for i in range(len(evList)):
            self.OD_3[evList[i].index] = self.GetKMDistance(depot, evList[i].destNode)
            
        # OD_4 setting
        for i in range(len(evList)):
            for j in range(len(evList)):
                if i != j:
                    self.OD_4[evList[i].index, evList[j].index] = self.GetKMDistance(evList[i].destNode, evList[j].rendezNode)
            
            
    def GetKMDistance(self, p1, p2):
        theta = p1.y - p2.y
        dist = math.sin(self.ConvertDecimalDegreesToRadians(p1.x)) * math.sin(self.ConvertDecimalDegreesToRadians(p2.x)) + math.cos(self.ConvertDecimalDegreesToRadians(p1.x)) * math.cos(self.ConvertDecimalDegreesToRadians(p2.x)) * math.cos(self.ConvertDecimalDegreesToRadians(theta))
        dist = math.acos(dist)
        dist = self.ConvertRadiansToDecimalDegrees(dist)
        dist = dist * 60 * 1.1515
        dist = dist * 1.609344

        return dist
    
    def ConvertDecimalDegreesToRadians(self, deg):
        return (deg * math.pi / 180)

    def ConvertRadiansToDecimalDegrees(self, rad):
        return (rad * 180 / math.pi)




class ODMatrix_MCS():
    def __init__(self, depot, evList, groundVehicleDistanceWeight):
        
        # (0, j+) : (depot node, rendezvous node of all customers)
        # n x 1 matrix (column)
        self.OD_1 = np.empty([len(evList)])
        self.OD_1.fill(100000000.0)
        
        
        # (j+, (j+1)+)) : (rendezvous node of a customer, rendezvous node of a proceeding customer)
        self.OD_2 = np.empty([len(evList), len(evList)])
        self.OD_2.fill(100000000.0)
        
        
        # OD_1 setting
        for i in range(len(evList)):
            self.OD_1[evList[i].index] = self.GetKMDistance(depot, evList[i].rendezNode) * groundVehicleDistanceWeight
            
            
        # OD_2 setting
        for i in range(len(evList)):
            for j in range(len(evList)):
                if evList[i].index < evList[j].index:
                    self.OD_2[evList[i].index, evList[j].index] = self.GetKMDistance(evList[i].rendezNode, evList[j].rendezNode) * groundVehicleDistanceWeight
            
            
            
    def GetKMDistance(self, p1, p2):
        theta = p1.y - p2.y
        dist = math.sin(self.ConvertDecimalDegreesToRadians(p1.x)) * math.sin(self.ConvertDecimalDegreesToRadians(p2.x)) + math.cos(self.ConvertDecimalDegreesToRadians(p1.x)) * math.cos(self.ConvertDecimalDegreesToRadians(p2.x)) * math.cos(self.ConvertDecimalDegreesToRadians(theta))
        dist = math.acos(dist)
        dist = self.ConvertRadiansToDecimalDegrees(dist)
        dist = dist * 60 * 1.1515
        dist = dist * 1.609344

        return dist
    
    def ConvertDecimalDegreesToRadians(self, deg):
        return (deg * math.pi / 180)

    def ConvertRadiansToDecimalDegrees(self, rad):
        return (rad * 180 / math.pi)
    