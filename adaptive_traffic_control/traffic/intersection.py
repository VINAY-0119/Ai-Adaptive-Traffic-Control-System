class Intersection:
    def __init__(self):
        self.current_phase = 'NS'
        self.phase_time = 0
        self.min_green = 5
        self.max_green = 30

    def can_switch(self):
        return self.phase_time >= self.min_green

    def switch(self):
        self.current_phase = 'EW' if self.current_phase == 'NS' else 'NS'
        self.phase_time = 0

    def step(self):
        self.phase_time += 1
