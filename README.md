# **HeatVision Proximity: Redefining Human Detection using Thermal sensor**

This project utilizes a Raspberry Pi Pico W microcontroller with an MLX90614 thermal sensor to monitor ambient and object temperatures. When the object temperature falls within a specified range, the script pushes a timestamp to Firebase Realtime Database and blinks an LED connected to GPIO pin 2.

## Prerequisites

Before running the project, ensure you have the following components:

-Raspberry Pi Pico W microcontroller

-MLX90614 thermal sensor

-LED (optional) for visual indication

-Wi-Fi network for internet connectivity

-Firebase Realtime Database for storing timestamps

-Firebase Storage to store images of the detected objects

-Link to Counterpart app:
```
https://github.com/astitva-sri/HeatVision-Proximity.git
```

## Setup

### Connect Hardware:

Connect the MLX90614 sensor to the Raspberry Pi Pico's I2C interface.
Optionally, connect an LED to GPIO pin 2 for visual indication.

### Configure Wi-Fi:

Update the Wi-Fi credentials in main.py to connect to your Wi-Fi network.

### Configure Firebase:

Update the Firebase API key, email, and password in firebase.py with your Firebase project details.

### Install Dependencies:

Install the required Python packages by running:

Copy code
```
pip install micropython-requests
```

## Usage

Flash the Python scripts (main.py, firebase.py, mlx90614.py, led.py, and wifi.py) to your Raspberry Pi Pico.
Connect the Pico to power.
The script will automatically start monitoring the temperature.
When the object temperature falls within the specified range, a timestamp will be pushed to Firebase Realtime Database, and the LED will blink.
You can view the timestamps in your Firebase project's Realtime Database.

## Reported Documents
You may access the reported documents about the completed projects, involving all the information needed

1. Project Report

[HeatVision Proximity P-09 (Report File).pdf](https://github.com/user-attachments/files/15585575/HeatVision.Proximity.P-09.Report.File.pdf)


2. Project Presentation

[HeatVision Proximity P-09 (Project PPT).pptx](https://github.com/user-attachments/files/15585579/HeatVision.Proximity.P-09.Project.PPT.pptx)


## Troubleshooting
If you encounter any issues with Wi-Fi connectivity or Firebase authentication, refer to the troubleshooting section in the README or review debug output for insights.
Ensure that the MLX90614 sensor is connected correctly and functioning properly.
#Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.










