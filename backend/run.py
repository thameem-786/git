from app import create_app, socketio
import os

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    
    # Seed demo data on startup
    with app.app_context():
        from app import db
        from app.models import User, Vehicle, Alert
        
        # Create demo users if they don't exist
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', role='admin')
            admin.set_password('admin123')
            db.session.add(admin)
        
        if not User.query.filter_by(username='engineer').first():
            engineer = User(username='engineer', role='engineer')
            engineer.set_password('eng123')
            db.session.add(engineer)
        
        if not User.query.filter_by(username='viewer').first():
            viewer = User(username='viewer', role='viewer')
            viewer.set_password('view123')
            db.session.add(viewer)
        
        db.session.commit()
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
