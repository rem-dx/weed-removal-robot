# Autonomous Weed Removal Robot
An autonomous robotics system that detects and removes weeds using computer vision and decision logic, supported by a synthetic field simulation for rapid development and testing.

## Demo / Output

This project was tested both in real-world conditions and using a synthetic field environment.

(Add images or screenshots of the robot, detection output, or field setup here if available.)

The system demonstrates end-to-end autonomy:
- weed detection
- decision-making
- actuation

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-orange)
![Robotics](https://img.shields.io/badge/Robotics-Autonomy-black)
![Simulation](https://img.shields.io/badge/Synthetic_Data-Simulation-lightgrey)

## Features

- Computer vision–based weed detection
- Autonomous decision logic for weed removal
- Synthetic field generation for testing and data augmentation
- Modular separation between vision, simulation, and control logic
- Designed to operate under real-world sensor and environmental constraints
- Supports rapid iteration without dependency on continuous field data collection

## Installation & Run

Clone the repository:
git clone https://github.com/rem-dx/autonomous-weed-removal-robot.git
cd autonomous-weed-removal-robot

Install dependencies:
pip install -r requirements.txt

Run the vision pipeline:
python vision/cv_pipeline.py

(Optional) Run synthetic field simulation:
python synthetic_field/field_generator.py

## How It Works

The system processes camera input to identify weeds using computer vision techniques.
Detected weeds are passed to a decision layer that determines when and how actuation should occur.
To accelerate development and reduce reliance on real-world data, a synthetic field environment was created to simulate crop and weed layouts.

Raw Camera Input / Synthetic Field
        ↓
Computer Vision Pipeline
        ↓
Weed Detection & Classification
        ↓
Decision Logic
        ↓
Actuation / Weed Removal

Final validation and deployment were performed on real-world hardware.

## Limitations

- Performance depends on lighting and camera quality
- Synthetic field does not capture all real-world variability
- No learning-based vision model included in current version
- Not optimized for large-scale agricultural deployment
