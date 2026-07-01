# Omokai GroundBot – LLM Powered Mission Executor

A ROS2-based autonomous mission executor capable of converting natural language instructions into executable navigation missions using a local Large Language Model (LLM).

---

# Overview

This project implements an end-to-end robotics pipeline that allows a user to issue high-level natural language commands such as:

> "Patrol the warehouse twice."

The system automatically:

1. Interprets the command using a local LLM (Mistral via Ollama)
2. Generates a structured mission in JSON format
3. Validates the generated mission
4. Converts it into ROS2 mission objects
5. Executes the mission using Nav2
6. Navigates a TurtleBot3 inside Gazebo

---

# Architecture

```
                User Prompt
                     │
                     ▼
            Mission Executor (ROS2)
                     │
                     ▼
            Mission Generator
                     │
                     ▼
          Ollama (Local Mistral LLM)
                     │
                     ▼
             JSON Mission Plan
                     │
                     ▼
             Mission Parser
                     │
                     ▼
             Mission Validator
                     │
                     ▼
              Mission Object
                     │
                     ▼
               Nav2 Client
                     │
                     ▼
              NavigateToPose
                     │
                     ▼
           TurtleBot3 + Gazebo
```

---

# Project Structure

```
omokai_executor/

├── executor.py
├── mission.py
├── mission_loader.py
├── mission_generator.py
├── nav_client.py
│
├── llm/
│   ├── ollama_client.py
│   ├── parser.py
│   ├── prompt.py
│   └── __init__.py
│
├── launch/
│   └── mission_executor.launch.py
│
├── package.xml
├── setup.py
└── README.md
```

---

# Features

- ROS2 Humble
- TurtleBot3 Gazebo simulation
- Nav2 integration
- Local LLM using Ollama
- Natural language mission planning
- JSON mission validation
- Multi-waypoint navigation
- Multi-lap patrol execution
- Modular ROS2 architecture

---

# Technologies Used

- ROS2 Humble
- Nav2
- Gazebo Classic
- TurtleBot3
- Python
- Ollama
- Mistral 7B

---

# Installation

Clone the repository:

```bash
git clone <repo-url>

cd omakai-groundbot/ros2_ws
```

Install dependencies:

```bash
sudo apt install python3-colcon-common-extensions
```

Build:

```bash
colcon build

source install/setup.bash
```

---

# Install Ollama

Install:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Download Mistral:

```bash
ollama pull mistral
```

Start the server:

```bash
ollama serve
```

---

# Running the Simulation

Launch Gazebo:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Launch Navigation2:

```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True
```

Initialize robot pose in RViz using **2D Pose Estimate**.

---

# Running the Mission Executor

Example:

```bash
ros2 launch omokai_executor mission_executor.launch.py \
prompt:="Patrol the warehouse twice"
```

---

# Example Prompt

Input:

```
Patrol the warehouse twice
```

Generated mission:

```json
{
    "mission_type": "patrol",
    "laps": 2,
    "speed": 0.5,
    "waypoints": [
        {
            "x": -1.0,
            "y": 0.0,
            "yaw": 0.0
        },
        {
            "x": 0.5,
            "y": 0.5,
            "yaw": 1.57
        },
        {
            "x": -1.0,
            "y": 1.0,
            "yaw": 3.14
        }
    ]
}
```

---

# Mission Execution Flow

```
Natural Language
        │
        ▼
Ollama (Mistral)
        │
        ▼
Mission JSON
        │
        ▼
Mission Validation
        │
        ▼
Mission Object
        │
        ▼
Nav2 Goals
        │
        ▼
Robot Navigation
```

---

# Validation

The parser validates:

- Valid JSON
- Required fields
- Mission type
- Number of laps
- Navigation speed
- Waypoint coordinates

Invalid missions are rejected before execution.

---

# Example Output

```
Generating mission...

Mission loaded successfully!

Waiting for Nav2...

Lap 1

Navigating to Loading Dock...

Goal completed.

Navigating to Storage Area...

Goal completed.

Mission completed.
```

---

# Future Improvements

- Dynamic obstacle avoidance
- Vision-based waypoint selection
- Function-calling LLM
- Automatic initial pose
- Semantic map understanding
- Multi-robot coordination
- Live mission replanning

---

# Notes

The project currently uses:

- Gazebo Classic
- TurtleBot3 Burger
- ROS2 Humble
- Nav2
- Ollama (local inference)

No cloud APIs are required.

---

# Demo

The recommended demo sequence is:

1. Launch Gazebo
2. Launch Nav2
3. Initialize robot pose
4. Start Ollama
5. Launch Mission Executor
6. Observe the robot complete the generated patrol mission

---

# Author

Joel Viju

ROS2 • Robotics • Autonomous Navigation • LLM Applications