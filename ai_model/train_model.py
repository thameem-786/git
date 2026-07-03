#!/usr/bin/env python3
"""
Train TensorFlow Lite model for vehicle health prediction
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras

def create_model(input_features=8):
    """
    Create neural network model
    Input: [temperature, voltage, current, vibration, rpm, coolant_temp, engine_load, fuel_level]
    Output: [health_score, failure_probability, fault_type, confidence]
    """
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=(input_features,)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(4, activation='sigmoid')  # 4 outputs
    ])
    
    model.compile(
        optimizer='adam',
        loss='mse',
        metrics=['mae']
    )
    
    return model

def generate_synthetic_data(n_samples=1000):
    """
    Generate synthetic training data
    """
    np.random.seed(42)
    
    # Features
    X = np.random.randn(n_samples, 8) * 20 + 100
    
    # Synthetic targets
    y = np.column_stack([
        np.random.uniform(50, 100, n_samples),  # health_score
        np.random.uniform(0, 0.5, n_samples),   # failure_probability
        np.random.uniform(0, 1, n_samples),     # fault_type (encoded)
        np.random.uniform(0.7, 1, n_samples)    # confidence
    ])
    
    return X, y

def train():
    """
    Train the model
    """
    print("Generating synthetic training data...")
    X, y = generate_synthetic_data(1000)
    
    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # Normalize
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    print("Creating model...")
    model = create_model()
    
    print("Training model...")
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))
    
    print("Evaluating...")
    loss, mae = model.evaluate(X_test, y_test)
    print(f"Test Loss: {loss:.4f}, MAE: {mae:.4f}")
    
    return model

def convert_to_tflite(model):
    """
    Convert Keras model to TensorFlow Lite
    """
    print("Converting to TFLite...")
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_model = converter.convert()
    
    with open('model.tflite', 'wb') as f:
        f.write(tflite_model)
    
    print("Model saved as model.tflite")

if __name__ == '__main__':
    model = train()
    convert_to_tflite(model)
