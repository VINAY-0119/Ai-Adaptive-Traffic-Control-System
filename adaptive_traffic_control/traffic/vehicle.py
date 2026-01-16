class Vehicle:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time
        self.waiting_time = 0

    def step(self):
        self.waiting_time += 1
