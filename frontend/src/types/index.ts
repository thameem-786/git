export interface User {
  id: string
  username: string
  role: 'admin' | 'engineer' | 'viewer'
}

export interface Vehicle {
  id: string
  name: string
  make: string
  model: string
  year: number
  vin: string
  mileage: number
}

export interface SensorData {
  id: string
  temperature: number
  voltage: number
  current: number
  vibration: number
  humidity: number
  pressure: number
  rpm: number
  speed: number
  coolant_temp: number
  fuel_level: number
  engine_load: number
  battery_voltage: number
  timestamp: string
}

export interface OBDData {
  id: string
  rpm: number
  speed: number
  coolant_temp: number
  engine_load: number
  fuel_level: number
  battery_voltage: number
  throttle_position: number
  dtc_codes: string[]
  timestamp: string
}

export interface Prediction {
  id: string
  health_score: number
  failure_probability: number
  fault_type: string
  confidence: number
  remaining_life: number
  recommendation: string
  timestamp: string
}

export interface Alert {
  id: string
  severity: 'low' | 'medium' | 'high' | 'critical'
  message: string
  component: string
  acknowledged: boolean
  timestamp: string
}

export interface DashboardData {
  vehicle: Vehicle
  health_score: number
  latest_sensors: SensorData
  latest_obd: OBDData
  latest_prediction: Prediction
  recent_alerts: Alert[]
  system_status: {
    engine: string
    battery: string
    brakes: string
    tyres: string
  }
}
