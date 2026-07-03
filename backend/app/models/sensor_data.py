from app import db
from datetime import datetime

class SensorData(db.Model):
    __tablename__ = 'sensor_data'
    
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    temperature = db.Column(db.Float, default=0.0)
    voltage = db.Column(db.Float, default=0.0)
    current = db.Column(db.Float, default=0.0)
    vibration = db.Column(db.Float, default=0.0)
    humidity = db.Column(db.Float, default=0.0)
    pressure = db.Column(db.Float, default=0.0)
    rpm = db.Column(db.Float, default=0.0)
    speed = db.Column(db.Float, default=0.0)
    coolant_temp = db.Column(db.Float, default=0.0)
    fuel_level = db.Column(db.Float, default=0.0)
    engine_load = db.Column(db.Float, default=0.0)
    battery_voltage = db.Column(db.Float, default=0.0)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'temperature': self.temperature,
            'voltage': self.voltage,
            'current': self.current,
            'vibration': self.vibration,
            'humidity': self.humidity,
            'pressure': self.pressure,
            'rpm': self.rpm,
            'speed': self.speed,
            'coolant_temp': self.coolant_temp,
            'fuel_level': self.fuel_level,
            'engine_load': self.engine_load,
            'battery_voltage': self.battery_voltage,
            'timestamp': self.timestamp.isoformat()
        }
