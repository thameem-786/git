from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO

db = SQLAlchemy()
jwt = JWTManager()
socketio = SocketIO()

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Load config
    if config_name == 'development':
        from app.config import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)
    elif config_name == 'production':
        from app.config import ProductionConfig
        app.config.from_object(ProductionConfig)
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")
    CORS(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    # Register blueprints
    from app.routes import auth_bp, dashboard_bp, sensors_bp, obd_bp, prediction_bp, alerts_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(sensors_bp)
    app.register_blueprint(obd_bp)
    app.register_blueprint(prediction_bp)
    app.register_blueprint(alerts_bp)
    
    # Register SocketIO events
    from app.websocket import events
    
    return app
