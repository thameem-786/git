from app import db
from datetime import datetime

class Prediction(db.Model):
    __tablename__ = 'predictions'
    
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    health_score = db.Column(db.Float, default=100.0)
    failure_probability = db.Column(db.Float, default=0.0)
    fault_type = db.Column(db.String(100), default='None')
    confidence = db.Column(db.Float, default=0.0)
    remaining_life = db.Column(db.Integer, default=0)  # in days
    recommendation = db.Column(db.Text, default='')
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'health_score': self.health_score,
            'failure_probability': self.failure_probability,
            'fault_type': self.fault_type,
            'confidence': self.confidence,
            'remaining_life': self.remaining_life,
            'recommendation': self.recommendation,
            'timestamp': self.timestamp.isoformat()
        }
