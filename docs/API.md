# EdgeGuardian AI - API Documentation

## Authentication

All endpoints (except `/api/auth/login`) require JWT authentication via the `Authorization` header:

```
Authorization: Bearer <token>
```

## Endpoints

### Authentication

#### POST /api/auth/login
Authenticate and receive JWT token.

**Request:**
```json
{
  "username": "admin",
  "password": "admin123"
}
```

**Response:**
```json
{
  "token": "eyJhbGc...",
  "user": {
    "id": 1,
    "username": "admin",
    "role": "admin",
    "created_at": "2024-01-01T00:00:00"
  }
}
```

#### POST /api/auth/register
Register a new user.

**Request:**
```json
{
  "username": "newuser",
  "password": "password123"
}
```

**Response:** Same as login

### Dashboard

#### GET /api/dashboard
Get complete dashboard data.

**Response:**
```json
{
  "vehicle": {...},
  "health_score": 94,
  "latest_sensors": {...},
  "latest_obd": {...},
  "latest_prediction": {...},
  "recent_alerts": [...],
  "system_status": {...}
}
```

### Sensors

#### GET /api/sensors
Get all sensor readings (paginated).

**Response:**
```json
[
  {
    "id": 1,
    "temperature": 85.5,
    "voltage": 13.8,
    "current": 45.2,
    "vibration": 2.1,
    "humidity": 55,
    "pressure": 32.5,
    "rpm": 2100,
    "speed": 60,
    "coolant_temp": 90,
    "fuel_level": 75,
    "engine_load": 45,
    "battery_voltage": 13.5,
    "timestamp": "2024-01-01T12:00:00"
  }
]
```

#### POST /api/sensors
Submit new sensor data.

**Request:** Same structure as GET response

### OBD Diagnostics

#### GET /api/obd
Get OBD-II diagnostic data.

**Response:**
```json
[
  {
    "id": 1,
    "rpm": 2100,
    "speed": 60,
    "coolant_temp": 90,
    "engine_load": 45,
    "fuel_level": 75,
    "battery_voltage": 13.5,
    "throttle_position": 25,
    "dtc_codes": [],
    "timestamp": "2024-01-01T12:00:00"
  }
]
```

### Predictions

#### GET /api/prediction
Get AI predictions.

**Response:**
```json
[
  {
    "id": 1,
    "health_score": 94,
    "failure_probability": 0.05,
    "fault_type": "None",
    "confidence": 0.98,
    "remaining_life": 365,
    "recommendation": "Vehicle is in excellent condition...",
    "timestamp": "2024-01-01T12:00:00"
  }
]
```

### Alerts

#### GET /api/alerts
Get vehicle alerts.

**Response:**
```json
[
  {
    "id": 1,
    "severity": "medium",
    "message": "Battery voltage low",
    "component": "Battery",
    "acknowledged": false,
    "timestamp": "2024-01-01T12:00:00"
  }
]
```

## WebSocket Events

### Connect
Initial connection to WebSocket server.

```javascript
const socket = io('http://localhost:5000');
socket.on('response', (data) => {
  console.log(data);
});
```

### sensor_update
Real-time sensor data broadcast.

```javascript
socket.on('sensor_update', (sensorData) => {
  console.log('New sensor data:', sensorData);
});
```

### alert_new
New alert notification.

```javascript
socket.on('alert_new', (alert) => {
  console.log('New alert:', alert);
});
```

### prediction_update
New prediction available.

```javascript
socket.on('prediction_update', (prediction) => {
  console.log('New prediction:', prediction);
});
```

## Error Responses

### 401 Unauthorized
```json
{
  "message": "Invalid credentials"
}
```

### 404 Not Found
```json
{
  "message": "Resource not found"
}
```

### 500 Server Error
```json
{
  "message": "Internal server error"
}
```
