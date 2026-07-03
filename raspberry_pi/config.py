class Config:
    """Raspberry Pi Configuration"""
    
    # API Configuration
    API_URL = 'http://localhost:5000'
    API_TOKEN = 'your-jwt-token-here'
    
    # Sensor Configuration
    SENSORS_ENABLED = {
        'temperature': True,
        'vibration': True,
        'voltage': True,
        'current': True,
        'obd': False  # Enable when ELM327 is connected
    }
    
    # GPIO Pins
    GPIO_PINS = {
        'temp_sensor': 4,      # DS18B20
        'vibration_sensor': 17,  # SW420
        'voltage_adc': 0,      # ADC Channel 0
        'current_adc': 1       # ADC Channel 1
    }
    
    # Sensor Parameters
    POLL_INTERVAL = 1  # seconds
    RETRY_ATTEMPTS = 3
    RETRY_DELAY = 5   # seconds
    
    # OBD-II Configuration
    OBD_PORT = '/dev/ttyUSB0'
    OBD_BAUDRATE = 38400
