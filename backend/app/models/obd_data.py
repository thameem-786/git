from app import db
from datetime import datetime

class OBDData(db.Model):
    __tablename__ = 'obd_data'
    
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    rpm = db.Column(db.Float, default=0.0)
    speed = db.Column(db.Float, default=0.0)
    coolant_temp = db.Column(db.Float, default=0.0)
    engine_load = db.Column(db.Float, default=0.0)
    fuel_level = db.Column(db.Float, default=0.0)
    battery_voltage = db.Column(db.Float, default=0.0)
    throttle_position = db.Column(db.Float, default=0.0)
    dtc_codes = db.Column(db.JSON, default=[])
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'rpm': self.rpm,
            'speed': self.speed,
            'coolant_temp': self.coolant_temp,
            'engine_load': self.engine_load,
            'fuel_level': self.fuel_level,
            'battery_voltage': self.battery_voltage,
            'throttle_position': self.throttle_position,
            'dtc_codes': self.dtc_codes,
            'timestamp': self.timestamp.isoformat()
        }
