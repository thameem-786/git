from flask import jsonify
from flask_jwt_extended import jwt_required
from app.models import Prediction, Vehicle
from app.routes import prediction_bp

@prediction_bp.route('', methods=['GET'])
@jwt_required()
def get_prediction():
    vehicle = Vehicle.query.first()
    if not vehicle:
        return jsonify({'message': 'No vehicle found'}), 404
    
    predictions = Prediction.query.filter_by(vehicle_id=vehicle.id).order_by(Prediction.timestamp.desc()).limit(10).all()
    return jsonify([pred.to_dict() for pred in predictions]), 200
