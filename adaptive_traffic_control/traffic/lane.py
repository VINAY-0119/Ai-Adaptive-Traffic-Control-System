from collections import deque

class Lane:
    def __init__(self, saturation_flow=1):
        self.queue = deque()
        self.saturation_flow = saturation_flow

    def add_vehicle(self, vehicle):
        self.queue.append(vehicle)

    def discharge(self):
        passed = []
        for _ in range(self.saturation_flow):
            if self.queue:
                passed.append(self.queue.popleft())
        return passed

    def update_waiting(self):
        for v in self.queue:
            v.step()

    def length(self):
        return len(self.queue)
