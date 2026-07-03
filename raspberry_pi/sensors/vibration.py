#!/usr/bin/env python3
"""
SW420 Vibration Sensor Reader
"""

import RPi.GPIO as GPIO
from config import Config

def read_vibration():
    """
    Read vibration level from SW420 sensor
    Returns digital signal (0 or 1)
    """
    try:
        GPIO.setmode(GPIO.BCM)
        pin = Config.GPIO_PINS['vibration_sensor']
        GPIO.setup(pin, GPIO.IN)
        
        vibration = GPIO.input(pin)
        GPIO.cleanup()
        
        return float(vibration)  # 0 or 1
    except Exception as e:
        print(f"Error reading vibration: {e}")
        return 0.0
