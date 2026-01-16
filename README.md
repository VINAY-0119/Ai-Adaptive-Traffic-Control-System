# Adaptive Traffic Signal Simulation (ATSS)

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modular Python framework for modeling, simulating, and optimizing traffic signal control strategies at four-way intersections. ATSS provides a robust testing environment for comparing traditional fixed-time controllers against adaptive algorithms using discrete-time simulation.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Extending the Framework](#extending-the-framework)
- [Performance Metrics](#performance-metrics)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Urban traffic congestion remains a critical infrastructure challenge, impacting economic productivity and environmental sustainability. The Adaptive Traffic Signal Simulation framework addresses this by providing a high-fidelity sandbox environment for testing and validating signal control algorithms.

ATSS simulates bi-directional traffic flows (North-South and East-West) and evaluates controller performance using metrics such as average vehicle delay and throughput. The framework's modular design enables seamless integration of advanced control strategies, from rule-based systems to deep reinforcement learning agents.

### Use Cases

- **Algorithm Benchmarking**: Compare fixed-time vs. adaptive control strategies
- **Research & Development**: Prototype and test novel traffic management algorithms
- **Educational Tool**: Demonstrate traffic engineering concepts and control theory
- **Policy Analysis**: Evaluate the impact of signal timing policies on traffic flow

---

## Key Features

### Simulation Engine

- **High-Fidelity Vehicle Modeling**: Individual vehicle tracking with precise wait-time metrics
- **FIFO Queue Management**: Realistic lane-level queuing behavior
- **Configurable Traffic Patterns**: Support for variable arrival rates and directional flows
- **Discrete-Time Stepping**: Deterministic simulation with configurable time resolution

### Signal Control

- **Two-Phase Operation**: Configurable North-South and East-West phases
- **Safety Constraints**: Enforced minimum and maximum green time intervals
- **Yellow/All-Red Phases**: Realistic transition periods for safety
- **Controller Abstraction**: Clean interface for implementing custom control logic

### Built-in Controllers

- **Fixed-Time Controller**: Traditional cycle-based signal timing
- **Rule-Based Adaptive Controller**: Real-time queue-responsive decision making
- **Extensible Framework**: Easy integration of custom algorithms and AI models

### Monitoring & Analytics

- **Virtual Sensors**: Real-time queue length and delay monitoring
- **Performance Metrics**: Automated calculation of average delay, throughput, and service rates
- **Data Export**: Simulation results available for external analysis

---

## Architecture

The framework employs a layered architecture to ensure separation of concerns and extensibility:

```
traffic_signal_sim/
│
├── main.py                      # Simulation orchestrator and entry point
│
├── simulation/                  # Core simulation engine
│   ├── simulator.py             # Discrete-time event processor
│   ├── intersection.py          # Signal phase state machine
│   ├── lane.py                  # Queue and capacity management
│   └── vehicle.py               # Individual vehicle entity
│
├── sensors/                     # Data acquisition layer
│   └── sensors.py               # Virtual sensors for queue/delay metrics
│
├── controllers/                 # Control strategy implementations
│   ├── base_controller.py       # Abstract controller interface
│   ├── fixed_time.py            # Static cycle controller
│   └── rule_based.py            # Adaptive threshold-based controller
│
├── metrics/                     # Performance analysis
│   └── performance.py           # Statistical metrics computation
│
├── tests/                       # Unit and integration tests
│   └── test_*.py                # Test suites
│
├── requirements.txt             # Python dependencies
└── README.md                    # Documentation
```

### Design Principles

- **Modularity**: Components are loosely coupled for independent testing and development
- **Extensibility**: Well-defined interfaces enable easy integration of new controllers
- **Realism**: Physics-based modeling captures real-world traffic dynamics
- **Performance**: Optimized for running large-scale simulations efficiently

---

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager
- (Optional) Virtual environment tool

### Step-by-Step Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/traffic_signal_sim.git
cd traffic_signal_sim
```

2. **Create a virtual environment** (recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Verify installation**

```bash
python -c "import numpy; print('Installation successful!')"
```

---

## Quick Start

Run a basic simulation with default parameters:

```bash
python main.py
```

**Expected Output:**

```
====================================
Traffic Signal Simulation Started
====================================
Controller: Rule-Based Adaptive
Simulation Duration: 500 steps
Traffic Pattern: Mixed (NS: 0.3, EW: 0.25 vehicles/step)

====================================
Simulation Complete
====================================
Total Vehicles Processed: 215
Average Delay per Vehicle: 14.2 seconds
Total Simulation Time: 500 steps
Throughput: 0.43 vehicles/step
```

---

## Usage

### Basic Configuration

Modify simulation parameters in `main.py`:

```python
from simulation.simulator import TrafficSimulator
from controllers.rule_based import RuleBasedController

# Initialize simulator
sim = TrafficSimulator(
    duration=1000,              # Simulation steps
    ns_arrival_rate=0.3,        # North-South arrival probability
    ew_arrival_rate=0.25,       # East-West arrival probability
    controller=RuleBasedController()
)

# Run simulation
results = sim.run()

# Access results
print(f"Average Delay: {results['avg_delay']:.2f}s")
print(f"Throughput: {results['throughput']:.2f} vehicles/step")
```

### Controller Selection

Switch between different control strategies:

```python
from controllers.fixed_time import FixedTimeController
from controllers.rule_based import RuleBasedController

# Use fixed-time controller
controller = FixedTimeController(
    ns_green_time=30,           # North-South green duration
    ew_green_time=25            # East-West green duration
)

# Use adaptive controller
controller = RuleBasedController(
    queue_threshold=5,          # Switch threshold
    min_green_time=10,          # Minimum green duration
    max_green_time=60           # Maximum green duration
)
```

### Advanced Scenarios

Configure complex traffic patterns:

```python
# Rush hour simulation
sim = TrafficSimulator(
    duration=2000,
    ns_arrival_rate=0.5,        # Heavy northbound traffic
    ew_arrival_rate=0.2,        # Light eastbound traffic
    controller=RuleBasedController()
)

# Balanced traffic
sim = TrafficSimulator(
    duration=1000,
    ns_arrival_rate=0.35,
    ew_arrival_rate=0.35,
    controller=FixedTimeController()
)
```

---

## Extending the Framework

### Creating Custom Controllers

Implement the controller interface to develop custom algorithms:

```python
from controllers.base_controller import BaseController

class MyCustomController(BaseController):
    """
    Custom traffic signal controller implementation.
    """
    
    def __init__(self, **kwargs):
        super().__init__()
        # Initialize controller parameters
        self.param1 = kwargs.get('param1', default_value)
    
    def decide(self, intersection, sensors):
        """
        Determine the optimal signal phase.
        
        Args:
            intersection: Current intersection state
            sensors: Real-time sensor data (queue lengths, delays)
        
        Returns:
            int: Phase selection (0 = NS, 1 = EW)
        """
        # Implement your control logic here
        ns_queue = sensors.get_queue_length('NS')
        ew_queue = sensors.get_queue_length('EW')
        
        # Example: Greedy queue-serving strategy
        if ns_queue > ew_queue:
            return 0  # Serve North-South
        else:
            return 1  # Serve East-West
    
    def reset(self):
        """Reset controller state between simulations."""
        pass
```

### Integration Example

```python
# Use custom controller in simulation
from my_controllers import MyCustomController

custom_controller = MyCustomController(param1=value)
sim = TrafficSimulator(
    duration=1000,
    controller=custom_controller
)
results = sim.run()
```

### Implementing Reinforcement Learning Agents

The framework supports RL integration through the controller interface:

```python
import gym
import numpy as np

class RLController(BaseController):
    """
    Reinforcement Learning controller wrapper.
    """
    
    def __init__(self, model):
        super().__init__()
        self.model = model  # Pre-trained RL model
    
    def decide(self, intersection, sensors):
        # Convert sensor data to observation vector
        state = self._get_state_vector(intersection, sensors)
        
        # Query RL model for action
        action = self.model.predict(state)
        
        return action
    
    def _get_state_vector(self, intersection, sensors):
        """Convert simulation state to RL observation."""
        return np.array([
            sensors.get_queue_length('NS'),
            sensors.get_queue_length('EW'),
            intersection.current_phase,
            intersection.phase_elapsed_time
        ])
```

---

## Performance Metrics

The framework automatically computes key performance indicators:

### Average Vehicle Delay

The mean time vehicles spend waiting in queue before crossing the intersection.

```
Average Delay = Σ(vehicle_wait_time) / total_vehicles
```

### Throughput

The number of vehicles processed per simulation step.

```
Throughput = total_vehicles_passed / simulation_duration
```

### Queue Statistics

- **Maximum Queue Length**: Peak queue size during simulation
- **Average Queue Length**: Mean queue size across all time steps
- **Queue Variance**: Measure of queue stability

### Accessing Metrics

```python
results = sim.run()

print(f"Performance Summary:")
print(f"  Average Delay: {results['avg_delay']:.2f}s")
print(f"  Max Queue (NS): {results['max_queue_ns']}")
print(f"  Max Queue (EW): {results['max_queue_ew']}")
print(f"  Throughput: {results['throughput']:.3f} veh/step")
```

---

## Roadmap

### Version 1.1 (Q2 2026)

- [ ] Real-time visualization using matplotlib/plotly
- [ ] Animated queue growth and signal phase transitions
- [ ] Interactive parameter tuning interface

### Version 1.2 (Q3 2026)

- [ ] OpenAI Gym environment wrapper for RL training
- [ ] Pre-trained RL agents (DQN, PPO, A3C)
- [ ] Benchmark suite comparing RL vs traditional controllers

### Version 2.0 (Q4 2026)

- [ ] Multi-intersection network simulation
- [ ] Coordinated signal control across corridors
- [ ] Vehicle routing and origin-destination modeling
- [ ] Support for pedestrian and bicycle traffic

### Future Enhancements

- Integration with SUMO (Simulation of Urban MObility)
- Real-world traffic data import (SCATS, ATMS)
- Cloud-based distributed simulation
- REST API for remote control and monitoring

---

## Contributing

We welcome contributions from the community! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:

- Code style and standards
- Testing requirements
- Pull request process
- Issue reporting

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run test suite
pytest tests/

# Run linter
flake8 traffic_signal_sim/

# Format code
black traffic_signal_sim/
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Citation

If you use ATSS in your research, please cite:

```bibtex
@software{atss2026,
  title = {Adaptive Traffic Signal Simulation Framework},
  author = {Your Name},
  year = {2026},
  url = {https://github.com/yourusername/traffic_signal_sim}
}
```

---


---

## Acknowledgments

- Inspired by classical traffic flow theory and modern adaptive control systems
- Built with Python and the scientific computing ecosystem (NumPy, SciPy, Matplotlib)
- Thanks to all contributors and the open-source community

---

**Made with ❤️ for smarter cities**
