#!/usr/bin/env python3
"""
Raspberry Pi Sensor Reader
Reads multiple sensors and posts data to Flask API
"""

import requests
import time
import json
import logging
from datetime import datetime
from sensors.temperature import read_temperature
from sensors.vibration import read_vibration
from sensors.voltage import read_voltage
from sensors.current import read_current
from config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SensorReader:
    def __init__(self, api_url=None):
        self.api_url = api_url or Config.API_URL
        self.sensors_enabled = Config.SENSORS_ENABLED
        self.poll_interval = Config.POLL_INTERVAL
    
    def read_all_sensors(self):
        """Read all available sensors"""
        sensor_data = {
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Read temperature
        if self.sensors_enabled.get('temperature'):
            try:
                sensor_data['temperature'] = read_temperature()
            except Exception as e:
                logger.error(f"Error reading temperature: {e}")
        
        # Read vibration
        if self.sensors_enabled.get('vibration'):
            try:
                sensor_data['vibration'] = read_vibration()
            except Exception as e:
                logger.error(f"Error reading vibration: {e}")
        
        # Read voltage
        if self.sensors_enabled.get('voltage'):
            try:
                sensor_data['voltage'] = read_voltage()
            except Exception as e:
                logger.error(f"Error reading voltage: {e}")
        
        # Read current
        if self.sensors_enabled.get('current'):
            try:
                sensor_data['current'] = read_current()
            except Exception as e:
                logger.error(f"Error reading current: {e}")
        
        return sensor_data
    
    def post_sensor_data(self, sensor_data):
        """Post sensor data to Flask API"""
        try:
            response = requests.post(
                f"{self.api_url}/api/sensors",
                json=sensor_data,
                headers={"Authorization": f"Bearer {Config.API_TOKEN}"},
                timeout=5
            )
            if response.status_code == 201:
                logger.info(f"Sensor data posted successfully")
            else:
                logger.error(f"Failed to post sensor data: {response.status_code}")
        except Exception as e:
            logger.error(f"Error posting sensor data: {e}")
    
    def run(self):
        """Main sensor reading loop"""
        logger.info("Starting sensor reader...")
        try:
            while True:
                sensor_data = self.read_all_sensors()
                self.post_sensor_data(sensor_data)
                time.sleep(self.poll_interval)
        except KeyboardInterrupt:
            logger.info("Sensor reader stopped")

if __name__ == '__main__':
    reader = SensorReader()
    reader.run()
