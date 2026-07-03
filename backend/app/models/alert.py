from app import db
from datetime import datetime

class Alert(db.Model):
    __tablename__ = 'alerts'
    
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    severity = db.Column(db.String(20), default='low')  # low, medium, high, critical
    message = db.Column(db.Text, nullable=False)
    component = db.Column(db.String(100), default='unknown')
    acknowledged = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'severity': self.severity,
            'message': self.message,
            'component': self.component,
            'acknowledged': self.acknowledged,
            'timestamp': self.timestamp.isoformat()
        }
