from flask_socketio import emit, on
from app import socketio

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('response', {'data': 'Connected to EdgeGuardian AI'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('request_update')
def handle_request_update():
    emit('response', {'data': 'Update requested'}, broadcast=True)
