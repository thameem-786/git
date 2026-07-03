from app import db
from datetime import datetime

class Maintenance(db.Model):
    __tablename__ = 'maintenance'
    
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    component = db.Column(db.String(100), nullable=False)
    action = db.Column(db.String(255), nullable=False)
    scheduled_date = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'component': self.component,
            'action': self.action,
            'scheduled_date': self.scheduled_date.isoformat(),
            'completed': self.completed,
            'notes': self.notes
        }
