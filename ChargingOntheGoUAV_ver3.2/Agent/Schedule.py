class Schedule():
    def __init__ (self):
        # 아래 정의된 순서대로 흐른다고 설정
        self.evIndex = 0
        self.rendezvous_arrivalTime = 0.0
        self.rendezvous_departureTime = 0.0
        self.destination_arrivalTime = 0.0
        self.destination_departureTime = 0.0
        self.depot_arrivalTime = 0.0
        self.depot_departureTime = 0.0
        