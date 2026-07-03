#!/usr/bin/env python3
"""
Voltage Sensor Reader (via ADC)
"""

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def read_voltage():
    """
    Read voltage from analog sensor via ADS1115 ADC
    """
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
        channel = AnalogIn(ads, ADS.P0)  # Channel 0
        
        # Read and convert to voltage
        voltage = channel.voltage
        return round(voltage, 2)
    except Exception as e:
        print(f"Error reading voltage: {e}")
        return 0.0
