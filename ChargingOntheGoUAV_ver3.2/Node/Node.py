class Node():
    def __init__ (self, type, x, y):
        self.type = type    # 0: depot, 1: rendezvous node, 2: destination node
        self.x = x
        self.y = y