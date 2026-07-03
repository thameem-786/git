from flask import jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models import Vehicle, SensorData, OBDData, Prediction, Alert
from app.routes import dashboard_bp
import random

@dashboard_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard():
    # Get first vehicle (demo)
    vehicle = Vehicle.query.first()
    if not vehicle:
        vehicle = Vehicle(
            name='Tesla Model 3',
            make='Tesla',
            model='Model 3',
            year=2023,
            vin='5YJ3E1EA7KF123456',
            mileage=15000
        )
        db.session.add(vehicle)
        db.session.commit()
    
    # Get latest sensor data or create dummy
    latest_sensor = SensorData.query.filter_by(vehicle_id=vehicle.id).order_by(SensorData.timestamp.desc()).first()
    if not latest_sensor:
        latest_sensor = SensorData(
            vehicle_id=vehicle.id,
            temperature=random.uniform(80, 100),
            voltage=random.uniform(12, 14),
            current=random.uniform(0, 100),
            vibration=random.uniform(0, 5),
            humidity=random.uniform(30, 70),
            pressure=random.uniform(30, 35),
            rpm=random.uniform(800, 3000),
            speed=random.uniform(0, 120),
            coolant_temp=random.uniform(85, 95),
            fuel_level=random.uniform(20, 100),
            engine_load=random.uniform(0, 100),
            battery_voltage=random.uniform(12, 14.5)
        )
        db.session.add(latest_sensor)
        db.session.commit()
    
    # Get latest OBD data
    latest_obd = OBDData.query.filter_by(vehicle_id=vehicle.id).order_by(OBDData.timestamp.desc()).first()
    if not latest_obd:
        latest_obd = OBDData(
            vehicle_id=vehicle.id,
            rpm=random.uniform(800, 3000),
            speed=random.uniform(0, 120),
            coolant_temp=random.uniform(85, 95),
            engine_load=random.uniform(0, 100),
            fuel_level=random.uniform(20, 100),
            battery_voltage=random.uniform(12, 14.5),
            throttle_position=random.uniform(0, 100),
            dtc_codes=[]
        )
        db.session.add(latest_obd)
        db.session.commit()
    
    # Get latest prediction
    latest_prediction = Prediction.query.filter_by(vehicle_id=vehicle.id).order_by(Prediction.timestamp.desc()).first()
    if not latest_prediction:
        latest_prediction = Prediction(
            vehicle_id=vehicle.id,
            health_score=94,
            failure_probability=0.05,
            fault_type='None',
            confidence=0.98,
            remaining_life=365,
            recommendation='Vehicle is in excellent condition. Regular maintenance recommended.'
        )
        db.session.add(latest_prediction)
        db.session.commit()
    
    # Get recent alerts
    recent_alerts = Alert.query.filter_by(vehicle_id=vehicle.id).order_by(Alert.timestamp.desc()).limit(5).all()
    
    return jsonify({
        'vehicle': vehicle.to_dict(),
        'health_score': latest_prediction.health_score,
        'latest_sensors': latest_sensor.to_dict(),
        'latest_obd': latest_obd.to_dict(),
        'latest_prediction': latest_prediction.to_dict(),
        'recent_alerts': [alert.to_dict() for alert in recent_alerts],
        'system_status': {
            'engine': 'Healthy',
            'battery': 'Healthy',
            'brakes': 'Healthy',
            'tyres': 'Healthy'
        }
    }), 200
