#!/usr/bin/env python3
"""
Current Sensor Reader (via ADC)
"""

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def read_current():
    """
    Read current from analog sensor via ADS1115 ADC
    """
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
        channel = AnalogIn(ads, ADS.P1)  # Channel 1
        
        # Read and convert to current (e.g., via current sensor chip)
        # Assuming ACS712 or similar: 5V = 0A, 2.5V = 0A at 185mV/A
        voltage = channel.voltage
        current = (voltage - 2.5) / 0.185  # Simplified conversion
        return round(current, 2)
    except Exception as e:
        print(f"Error reading current: {e}")
        return 0.0
