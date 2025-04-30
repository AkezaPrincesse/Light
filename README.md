#  Light 

This project simulates a real-world IoT dashboard that lets users schedule a light ON/OFF cycle using a web interface. It uses WebSockets, MQTT, and serial communication with an Arduino (or simulation).

## Features

- HTML dashboard to set ON and OFF times
- Real-time communication via WebSockets
- MQTT messaging using `mosquitto_pub/sub`
- Python backend to relay commands to Arduino via serial
- Arduino listens to `'1'` or `'0'` and toggles a relay

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (`websockets`, `pyserial`, `subprocess`)
- **Communication**: MQTT (`mosquitto_pub`, `mosquitto_sub`)
- **Device**: Arduino UNO
- **Simulation**: Virtual COM ports (e.g., VSPE/com0com)

---


---

## Setup Instructions

### 1. Prerequisites

- Python 3.8+
- Arduino IDE (if using real hardware)
- Mosquitto MQTT installed (`mosquitto_pub`, `mosquitto_sub`)
- Optional: [VSPE](http://www.eterlogic.com/Products.VSPE.html) or [com0com](https://com0com.sourceforge.net/) for serial simulation

### 2. Install Python Requirements

```bash
pip install websockets pyserial

### 3. If no Arduino is connected, run:
python arduino_simulator.py

### Author
# AKEZA Aimee Princesse


