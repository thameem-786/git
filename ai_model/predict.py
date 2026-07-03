#!/usr/bin/env python3
"""
TFLite Model Inference
"""

import numpy as np
import tensorflow as tf

class VehiclePredictor:
    def __init__(self, model_path='model.tflite'):
        """Load TFLite model"""
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
    
    def predict(self, sensor_data):
        """
        Predict vehicle health
        sensor_data: dict with keys [temperature, voltage, current, vibration, rpm, coolant_temp, engine_load, fuel_level]
        """
        # Prepare input
        features = np.array([
            sensor_data.get('temperature', 0),
            sensor_data.get('voltage', 0),
            sensor_data.get('current', 0),
            sensor_data.get('vibration', 0),
            sensor_data.get('rpm', 0),
            sensor_data.get('coolant_temp', 0),
            sensor_data.get('engine_load', 0),
            sensor_data.get('fuel_level', 0)
        ], dtype=np.float32).reshape(1, -1)
        
        # Run inference
        self.interpreter.set_tensor(self.input_details[0]['index'], features)
        self.interpreter.invoke()
        
        # Get output
        output = self.interpreter.get_tensor(self.output_details[0]['index'])
        
        # Parse results
        return {
            'health_score': float(output[0][0] * 100),
            'failure_probability': float(output[0][1]),
            'fault_type': 'Engine' if output[0][2] > 0.5 else 'Battery',
            'confidence': float(output[0][3])
        }

if __name__ == '__main__':
    predictor = VehiclePredictor()
    
    test_data = {
        'temperature': 85,
        'voltage': 13.5,
        'current': 50,
        'vibration': 2.1,
        'rpm': 2000,
        'coolant_temp': 90,
        'engine_load': 45,
        'fuel_level': 75
    }
    
    result = predictor.predict(test_data)
    print("Prediction Result:")
    for key, value in result.items():
        print(f"  {key}: {value}")
