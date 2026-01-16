from core.simulator import Simulator
from controllers.rule_based import RuleBasedController
from sensors.sensors import get_queue_lengths
from evaluation.metrics import average_delay

SIM_TIME = 2000

sim = Simulator(arrival_rate=0.4)
controller = RuleBasedController()

for _ in range(SIM_TIME):
    queues = get_queue_lengths(sim.lanes)
    controller.decide(sim.intersection, queues)
    sim.step()

print("Simulation complete")
print("Vehicles passed:", len(sim.completed))
print("Average delay:", average_delay(sim.completed))
