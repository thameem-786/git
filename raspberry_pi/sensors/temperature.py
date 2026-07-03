#!/usr/bin/env python3
"""
DS18B20 Temperature Sensor Reader
"""

import os
import glob

def read_temperature():
    """
    Read temperature from DS18B20 sensor
    Uses 1-wire protocol via GPIO 4
    """
    try:
        # Find the device file
        device_files = glob.glob('/sys/bus/w1/devices/28-*/w1_slave')
        if not device_files:
            return 0.0
        
        device_file = device_files[0]
        
        # Read the device file
        with open(device_file, 'r') as f:
            lines = f.readlines()
        
        # Parse temperature from the second line
        if lines[0].strip()[-3:] == 'YES':
            temp_pos = lines[1].find('t=')
            if temp_pos != -1:
                temp_string = lines[1][temp_pos+2:]
                temp_c = float(temp_string) / 1000.0
                return temp_c
        return 0.0
    except Exception as e:
        print(f"Error reading temperature: {e}")
        return 0.0
