from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app import db, socketio
from app.models import SensorData, Vehicle
from app.routes import sensors_bp

@sensors_bp.route('', methods=['GET'])
@jwt_required()
def get_sensors():
    vehicle = Vehicle.query.first()
    if not vehicle:
        return jsonify({'message': 'No vehicle found'}), 404
    
    sensors = SensorData.query.filter_by(vehicle_id=vehicle.id).order_by(SensorData.timestamp.desc()).limit(100).all()
    return jsonify([sensor.to_dict() for sensor in sensors]), 200

@sensors_bp.route('', methods=['POST'])
@jwt_required()
def post_sensor():
    data = request.get_json()
    vehicle = Vehicle.query.first()
    if not vehicle:
        return jsonify({'message': 'No vehicle found'}), 404
    
    sensor = SensorData(
        vehicle_id=vehicle.id,
        temperature=data.get('temperature', 0),
        voltage=data.get('voltage', 0),
        current=data.get('current', 0),
        vibration=data.get('vibration', 0),
        humidity=data.get('humidity', 0),
        pressure=data.get('pressure', 0),
        rpm=data.get('rpm', 0),
        speed=data.get('speed', 0),
        coolant_temp=data.get('coolant_temp', 0),
        fuel_level=data.get('fuel_level', 0),
        engine_load=data.get('engine_load', 0),
        battery_voltage=data.get('battery_voltage', 0)
    )
    db.session.add(sensor)
    db.session.commit()
    
    # Broadcast via WebSocket
    socketio.emit('sensor_update', sensor.to_dict(), broadcast=True)
    
    return jsonify(sensor.to_dict()), 201
