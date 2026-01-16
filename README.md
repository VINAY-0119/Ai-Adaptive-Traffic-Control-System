Adaptive Traffic Signal Simulation

This project is a Python-based simulation framework for adaptive traffic signal control. It models vehicle flow through an intersection, supports multiple control algorithms, and provides a foundation for experimenting with intelligent traffic management.

Features

Simulates vehicle arrivals and movement through a two-phase traffic intersection (North-South and East-West).

Includes basic vehicle and lane models with waiting time tracking.

Implements fixed-time and rule-based adaptive signal controllers.

Supports sensor-like functions for queue length and delay measurement.

Measures performance through average vehicle delay.

Fully modular and extensible architecture.

Project Structure
traffic_signal_sim/
│
├── main.py                    # Main script to run the simulation
│
├── simulation/                # Core simulation components
│   ├── __init__.py
│   ├── simulator.py           # Simulator engine managing time steps
│   ├── intersection.py       # Intersection and signal phase logic
│   ├── lane.py               # Lane queue management
│   └── vehicle.py            # Vehicle model with waiting time
│
├── sensors/                  # Virtual sensor modules
│   ├── __init__.py
│   └── sensors.py            # Functions to measure queues and delay
│
├── controllers/              # Traffic signal control algorithms
│   ├── __init__.py
│   ├── fixed_time.py         # Fixed-cycle controller implementation
│   └── rule_based.py         # Rule-based adaptive controller
│
├── metrics/                  # Performance metrics calculations
│   ├── __init__.py
│   └── performance.py        # Average delay calculation
│
└── requirements.txt          # Project dependencies (numpy, matplotlib)

Installation

Clone or download this repository.

Create and activate a Python environment (recommended).

Install dependencies:

pip install -r requirements.txt

Usage

Run the simulation from the command line:

python main.py


The simulation will run for a predefined time (default 500 steps) using the rule-based adaptive controller. Output includes total vehicles passed and average delay.

How It Works

Simulator manages the overall flow: vehicle generation, movement, and time progression.

Intersection handles signal phases and timing constraints.

Lanes maintain queues of vehicles.

Vehicles track their own waiting time.

Controllers decide when to switch signal phases based on fixed timing or adaptive rules.

Sensors provide current queue lengths and delays to controllers.

Metrics evaluate performance after the simulation ends.

Extending the Project

You can add more sophisticated control algorithms by creating new controller classes under controllers/. Use the sensor functions to get traffic state information and call intersection.switch_phase() to change signals.

Example extension points:

Implement a machine learning-based controller.

Add pedestrian crossing phases.

Model multiple intersections and network effects.

Visualize traffic flow using matplotlib.
