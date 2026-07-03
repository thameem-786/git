from flask import jsonify
from flask_jwt_extended import jwt_required
from app.models import Alert, Vehicle
from app.routes import alerts_bp

@alerts_bp.route('', methods=['GET'])
@jwt_required()
def get_alerts():
    vehicle = Vehicle.query.first()
    if not vehicle:
        return jsonify({'message': 'No vehicle found'}), 404
    
    alerts = Alert.query.filter_by(vehicle_id=vehicle.id).order_by(Alert.timestamp.desc()).limit(20).all()
    return jsonify([alert.to_dict() for alert in alerts]), 200
