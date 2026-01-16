class RuleBasedController:
    def __init__(self, threshold=5):
        self.threshold = threshold

    def decide(self, intersection, queues):
        current = intersection.current_phase
        other = 'EW' if current == 'NS' else 'NS'
        if intersection.phase_time >= intersection.max_green:
            intersection.switch()
        elif queues[other] > self.threshold and intersection.can_switch():
            intersection.switch()
