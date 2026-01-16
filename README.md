Adaptive Traffic Signal Simulation (ATSS)
An extensible Python framework designed to model, simulate, and optimize traffic signal control logic at a four-way intersection. This project provides a sandbox for testing Fixed-Time vs. Adaptive control strategies using discrete-time simulation.

📌 Overview
Urban congestion is a multi-billion dollar problem. The ATSS Framework allows users to simulate North-South (NS) and East-West (EW) traffic flows to evaluate how different signal algorithms impact vehicle latency. By utilizing a modular architecture, the simulation can be easily extended from simple rule-based logic to complex Reinforcement Learning (RL) models.

🚀 Key Features
High-Fidelity Modeling: Individual vehicle tracking with cumulative wait-time metrics and FIFO (First-In-First-Out) lane queuing.

Dynamic Signal Phases: Configurable two-phase system (NS/EW) with safety constraints like minimum/maximum green times.

Pluggable Controllers: * Fixed-Time: Traditional cycle-based approach.

Rule-Based Adaptive: Reacts to real-time sensor data to minimize active queues.

Virtual Sensing: Integrated hooks for queue length detection and cumulative delay monitoring.

Data-Driven Metrics: Automated calculation of Average Vehicle Delay, providing immediate feedback on algorithm efficiency.

📂 Project Structure
The project follows a decoupled architecture to ensure that the simulation engine is independent of the control logic.

Plaintext

traffic_signal_sim/
├── main.py                # Simulation entry point
├── simulation/            # Core Physics & Logic
│   ├── simulator.py       # Engine handling discrete time steps
│   ├── intersection.py    # Signal phase state machine
│   ├── lane.py            # Queue management
│   └── vehicle.py         # Vehicle attribute tracking
├── sensors/               # Data Acquisition
│   └── sensors.py         # Virtual sensors for queue/delay metrics
├── controllers/           # Intelligence Layer
│   ├── fixed_time.py      # Static cycle implementation
│   └── rule_based.py      # Adaptive logic
├── metrics/               # Analytics
│   └── performance.py     # Average delay & throughput calculations
└── requirements.txt       
🛠️ Getting Started
Prerequisites
Python 3.7 or higher

NumPy

Installation
Clone the repository

Bash

git clone https://github.com/yourusername/traffic_signal_sim.git
cd traffic_signal_sim
Set up environment (Optional but recommended)

Bash

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
Running the Simulation
Execute the default simulation (500 steps) using the Rule-Based controller:

Bash

python main.py
Example Output:

Simulation Complete. Total Vehicles Processed: 142 Average Delay: 18.4 seconds/vehicle

🔧 Extension Guide
Adding a Custom Controller
The framework is designed for experimentation. To create a new controller (e.g., AI-based), inherit from the base controller logic and implement the decide method:

Python

class MyCustomController:
    def decide(self, intersection, queues):
        # Your logic here
        # Return 0 for Phase NS, 1 for Phase EW
        pass
Future Roadmap
[ ] Visualization: Integration with matplotlib for real-time queue graphing.

[ ] Network Expansion: Support for multi-intersection "Green Wave" coordination.

[ ] ML Integration: OpenAI Gym-compatible wrapper for Reinforcement Learning training.
