cat > README.md << EOF
# Adaptive Traffic Signal Simulation (ATSS)

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)  
![License](https://img.shields.io/badge/license-MIT-green)

This project presents a Python framework designed to model, simulate, and optimize traffic signal control at a four-way intersection. It enables comparison between Fixed-Time and Adaptive traffic control strategies through discrete-time simulation.

---

## Overview

Traffic congestion is a critical issue in urban environments. The ATSS framework simulates traffic flows in North-South (NS) and East-West (EW) directions, providing a platform to assess the impact of various signal control algorithms on vehicle delay. Its modular design facilitates easy extension from simple rule-based methods to advanced reinforcement learning techniques.

---

## Key Features

- Detailed Vehicle Modeling: Tracks individual vehicles with wait time accumulation and FIFO lane queuing.
- Configurable Signal Phases: Implements a two-phase system (NS/EW) with configurable minimum and maximum green durations.
- Modular Controllers:  
  - Fixed-Time: Traditional cyclic control strategy.  
  - Rule-Based Adaptive: Dynamic adjustment based on real-time sensor data.
- Virtual Sensors: Integrated mechanisms for queue length and delay monitoring.
- Performance Metrics: Automatic computation of average vehicle delay to evaluate control efficiency.

---

## Project Structure

\`\`\`
traffic_signal_sim/
├── main.py                # Simulation entry point
├── simulation/
│   ├── simulator.py       # Discrete time-step simulation engine
│   ├── intersection.py    # Traffic signal phase management
│   ├── lane.py            # Vehicle queue management
│   └── vehicle.py         # Vehicle attribute tracking
├── sensors/
│   └── sensors.py         # Virtual sensors for queue and delay measurement
├── controllers/
│   ├── fixed_time.py      # Fixed-Time signal controller
│   └── rule_based.py      # Adaptive rule-based controller
├── metrics/
│   └── performance.py     # Delay and throughput analytics
└── requirements.txt
\`\`\`

---

## Getting Started

### Prerequisites

- Python 3.7 or later  
- NumPy library

### Installation

Clone the repository:

\`\`\`bash
git clone https://github.com/yourusername/traffic_signal_sim.git
cd traffic_signal_sim
\`\`\`

(Optional) Create and activate a virtual environment:

\`\`\`bash
python -m venv venv
# Windows:
venv\\Scripts\\activate
# macOS/Linux:
source venv/bin/activate
\`\`\`

Install dependencies:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### Running the Simulation

Execute the simulation using the default rule-based adaptive controller:

\`\`\`bash
python main.py
\`\`\`

Expected output:

\`\`\`
Simulation finished for 500 steps. Total Vehicles Passed: 215 Average Delay per Vehicle: 14.2s
\`\`\`

---

## Extending the Framework

To implement a custom control algorithm, create a new class within the \`controllers/\` directory and define the \`decide\` method:

\`\`\`python
class CustomController:
    def decide(self, intersection, queues):
        # Define logic to select signal phase
        # Return 0 for North-South, 1 for East-West
        pass
\`\`\`

---

## Future Enhancements

- Integration of real-time visualization using matplotlib  
- Development of reinforcement learning agents with OpenAI Gym wrappers  
- Expansion to multi-intersection simulations for urban corridor modeling

---
EOF
