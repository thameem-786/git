from app import db
from datetime import datetime

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    vin = db.Column(db.String(17), unique=True, nullable=False)
    mileage = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    sensor_data = db.relationship('SensorData', backref='vehicle', lazy=True, cascade='all, delete-orphan')
    obd_data = db.relationship('OBDData', backref='vehicle', lazy=True, cascade='all, delete-orphan')
    predictions = db.relationship('Prediction', backref='vehicle', lazy=True, cascade='all, delete-orphan')
    alerts = db.relationship('Alert', backref='vehicle', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'vin': self.vin,
            'mileage': self.mileage
        }
