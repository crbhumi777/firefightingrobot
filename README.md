
# **Fire Fighting Robot 🚒🤖**

The **Fire Fighting Robot** is an autonomous robot designed to detect and extinguish fires in hazardous areas, all without the need for human intervention. Using a **Raspberry Pi**, **Python**, and **OpenCV**, this robot navigates through dangerous environments, detects fire, and activates its extinguisher to put it out. The robot is equipped with a camera to detect fires and people in fire-affected areas, allowing it to avoid obstacles and reach the fire source.

---

## **Project Overview**
The current trend is to utilize robots in place of humans to handle fire dangers, especially in situations where human presence is too risky. This project aims to create a robot capable of:
- **Detecting fires and human** in specific areas.
- **Navigating autonomously** while avoiding obstacles.
- **Extinguishing fires** using a pump extinguisher attached to the robot.
- **Serving as a first-response vehicle** for fire emergencies, reducing the need for human firefighters to enter hazardous zones.

The Raspberry Pi board serves as the robot's control center, while the integrated camera uses computer vision to detect persons in fire-affected regions and move the robot to the target location.

---

## **Features**
- **Autonomous Navigation**: The robot can move around, avoid obstacles, and reach fire-damaged areas.
- **Fire and face Detection**: Using a camera and Python/OpenCV, the robot detects fire and people.
- **Fire Extinguishing**: A pump extinguisher is activated when the robot approaches the fire and people.
- **Remote Control (Optional)**: The robot can be controlled remotely for manual interventions.
- **Compact Design**: Small size allows the robot to operate in narrow and restricted spaces.

---

## **Tech Stack**
- **Hardware**: Raspberry Pi (Control Board), Camera (for fire detection), Pump Extinguisher
- **Software**: Python, OpenCV (for computer vision)
- **Navigation**: Autonomous path planning and obstacle avoidance

---

## **How It Works**

- The camera detects **fire** using computer vision techniques (OpenCV).
- The robot navigates toward the **fire location** and avoids obstacles in its path.
- Once the robot reaches the fire, it **activates the pump extinguisher** to put out the flames.
- The robot can also be **controlled remotely** for specific tasks.
