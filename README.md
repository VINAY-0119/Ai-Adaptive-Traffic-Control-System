cat > README.md << 'EOF'
# Adaptive Traffic Signal Simulation (ATSS)

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)  
![License](https://img.shields.io/badge/license-MIT-green)

An extensible Python framework to model and simulate traffic signals at a four-way intersection. It supports Fixed-Time and Adaptive control strategies with discrete-time simulation.

---

## Overview

Urban congestion is a major challenge. The ATSS Framework simulates North-South (NS) and East-West (EW) traffic flows to evaluate how signal algorithms affect vehicle delay. Its modular design supports everything from rule-based logic to reinforcement learning.

---

## Key Features

- High-Fidelity Modeling: Tracks individual vehicles with wait times and FIFO lane queues.
- Dynamic Signal Phases: Two-phase system (NS/EW) with minimum and maximum green times.
- Pluggable Controllers:  
  - Fixed-Time: traditional cycle-based control  
  - Rule-Based Adaptive: reacts to sensor data to reduce queues
- Virtual Sensors: Measure queue length and cumulative delays.
- Performance Metrics: Automatically calculates average vehicle delay.

---

## Project Structure

\`\`\`
traffic_signal_sim/
├── main.py                # Simulation entry point
├── simulation/
│   ├── simulator.py       # Discrete time-step engine
│   ├── intersection.py    # Signal state machine
│   ├── lane.py            # Queue management
│   └── vehicle.py         # Vehicle tracking
├── sensors/
│   └── sensors.py         # Virtual queue/delay sensors
├── controllers/
│   ├── fixed_time.py      # Static cycle controller
│   └── rule_based.py      # Adaptive controller
├── metrics/
│   └── performance.py     # Delay and throughput calculations
└── requirements.txt
\`\`\`

---

## Getting Started

### Prerequisites

- Python 3.7+  
- NumPy

### Installation

\`\`\`bash
git clone https://github.com/yourusername/traffic_signal_sim.git
cd traffic_signal_sim
\`\`\`

(Optional) Create and activate a virtual environment:

\`\`\`bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
\`\`\`

Install dependencies:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### Running the Simulation

\`\`\`bash
python main.py
\`\`\`

Expected output:

\`\`\`
Simulation finished for 500 steps. Total Vehicles Passed: 215 Average Delay per Vehicle: 14.2s
\`\`\`

---

## Extending the Simulation

Create a new controller by adding a class in \`controllers/\` implementing the \`decide\` method:

\`\`\`python
class MyAIController:
    def decide(self, intersection, queues):
        # Implement logic to decide phase
        # Return 0 for North-South or 1 for East-West
        pass
\`\`\`

---

## Future Roadmap

- Visualization with matplotlib for real-time queue graphs  
- Reinforcement Learning agent using OpenAI Gym wrappers  
- Multi-intersection simulation to model city corridors

---
EOF
