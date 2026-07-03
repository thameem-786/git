from flask import jsonify
from flask_jwt_extended import jwt_required
from app.models import OBDData, Vehicle
from app.routes import obd_bp

@obd_bp.route('', methods=['GET'])
@jwt_required()
def get_obd():
    vehicle = Vehicle.query.first()
    if not vehicle:
        return jsonify({'message': 'No vehicle found'}), 404
    
    obd_data = OBDData.query.filter_by(vehicle_id=vehicle.id).order_by(OBDData.timestamp.desc()).limit(100).all()
    return jsonify([data.to_dict() for data in obd_data]), 200
