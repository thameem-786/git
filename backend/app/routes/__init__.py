from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/api')
sensors_bp = Blueprint('sensors', __name__, url_prefix='/api/sensors')
obd_bp = Blueprint('obd', __name__, url_prefix='/api/obd')
prediction_bp = Blueprint('prediction', __name__, url_prefix='/api/prediction')
alerts_bp = Blueprint('alerts', __name__, url_prefix='/api/alerts')

from app.routes import auth, dashboard, sensors, obd, prediction, alerts
