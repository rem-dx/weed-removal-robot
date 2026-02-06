# Autonomous Weed Removal Robot 🌱🤖

## Overview
Autonomous weed removal robot using real-time computer vision.
The system detects weeds between crop rows and selectively activates
a mechanical rotor while prioritizing crop safety.

Designed for edge deployment on Raspberry Pi with low compute overhead.


![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![OpenCV](https://img.shields.io/badge/opencv-computer%20vision-green)
![Robotics](https://img.shields.io/badge/domain-robotics-orange)
![Status](https://img.shields.io/badge/status-active-success)


## Key Features
- Real-time weed detection using OpenCV
- Crop vs weed separation using spatial logic
- Kill-zone based mechanical actuation
- Autonomous and manual (operator-controlled) modes
- No dataset collection or model training required

## Tech Stack
- Python
- OpenCV
- NumPy
- Raspberry Pi (deployment)
- Arduino (motor control)

## How It Works
1. Camera captures ground view
2. Green vegetation is detected using OpenCV
3. Spatial rules identify crop rows vs weeds
4. Rotor activates only when weeds enter the kill zone

## Project Structure
weed_robot_ai/
- main.py              # Entry point
- synthetic_field.py   # Synthetic test field (no hardware required)
- vision_utils.py      # Vision utilities
- weed_detector.py     # Decision logic

## Running Locally
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install opencv-python numpy
python main.py

## Modes
- Autonomous: Vision-based weed removal
- Manual: Operator override for safety and testing

## Use Cases
- Precision agriculture
- Autonomous field robots
- Robotics competitions
- Edge AI demonstrations
