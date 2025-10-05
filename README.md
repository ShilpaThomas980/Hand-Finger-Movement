# Hand Tracking & Finger Accuracy Game

## Project Aim
This project is an interactive hand-tracking application using Python. The main goal is to track finger movements in real-time and measure accuracy while tracing different shapes on the screen. It also includes controlling system volume with finger gestures.

---

## Files Overview

### 1. `main.py`
- The main script that runs the application.
- Captures video from the webcam.
- Integrates all modules (`hand_detection`, `volume`, `fps`, `shape_manager`).
- Displays the shapes, accuracy, FPS, and volume control in real-time.

### 2. `hand_detection.py`
- Detects hands and finger landmarks using Mediapipe.
- Draws colored dots for each finger and lines connecting joints.
- Returns fingertip positions for accuracy calculations.

### 3. `volume.py`
- Controls system volume based on the distance between the thumb and index finger.
- Updates the volume smoothly in real-time.

### 4. `fps.py`
- Calculates and displays the frames per second (FPS) on the screen.
- Helps monitor the performance of the application.

### 5. `accuracy.py`
- Calculates how accurately the user traces the target shape.
- Compares fingertip positions with the target path and outputs a score.

### 6. `shapes.py`
- Contains functions to generate different shapes: circle, square, line, triangle.
- Returns coordinates of points forming each shape.

### 7. `shape_manager.py`
- Manages automatic shape display and countdown.
- Displays a countdown (3, 2, 1) before showing each shape.
- Switches to the next shape every 8 seconds.
- Calculates accuracy in real-time.

---

## Features
- Real-time hand and finger tracking.
- Automatic display of different shapes with countdown.
- Accuracy measurement while tracing shapes.
- System volume control using finger gestures.
- FPS display for performance monitoring.

---

## Requirements
- Python 3.x
- OpenCV
- Mediapipe
- NumPy
- Optional: `nircmd.exe` (for Windows volume control)

---

## How to Run
1. Clone the repository.
2. Install dependencies:
