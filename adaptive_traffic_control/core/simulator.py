import random
from traffic.vehicle import Vehicle
from traffic.lane import Lane
from traffic.intersection import Intersection

class Simulator:
    def __init__(self, arrival_rate=0.3):
        self.time = 0
        self.arrival_rate = arrival_rate
        self.intersection = Intersection()
        self.lanes = {'NS': Lane(), 'EW': Lane()}
        self.completed = []

    def generate_traffic(self):
        for d in self.lanes:
            if random.random() < self.arrival_rate:
                self.lanes[d].add_vehicle(Vehicle(self.time))

    def move_traffic(self):
        green = self.intersection.current_phase
        passed = self.lanes[green].discharge()
        self.completed.extend(passed)
        for lane in self.lanes.values():
            lane.update_waiting()

    def step(self):
        self.generate_traffic()
        self.move_traffic()
        self.intersection.step()
        self.time += 1
