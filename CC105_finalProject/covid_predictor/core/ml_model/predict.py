import pickle
import numpy as np
import os
import traceback

# Load the models
def load_model():
    try:
        model_path = os.path.join(os.path.dirname(__file__), 'covid_symptom_predictor.pkl')
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        print("Model loaded successfully.")
        
        scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')
        with open(scaler_path, 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)
        print("Scaler loaded successfully.")
        
        return model, scaler
    except Exception as e:
        print(f"Error loading model or scaler: {e}")
        traceback.print_exc()
        raise  # Re-raise the exception after logging it


# Function to predict the result based on user input
def predict_result(input_data):
    try:
        # Ensure input_data is a list of numerical values and check if it is passed correctly
        print(f"Initial input data: {input_data}")
        
        # Check if the length of input_data matches the expected number of features
        expected_features = 10  # Set the expected number of features based on your model input
        if len(input_data) != expected_features:
            raise ValueError(f"Expected {expected_features} features, but got {len(input_data)}.")
        
        model, scaler = load_model()
        
        print("Input data:", input_data)
        
        # Convert input to NumPy array and reshape
        input_data = np.array(input_data).reshape(1, -1)
        print(f"Reshaped input data: {input_data.shape}")  # Check input shape
        
        # Scale the input
        scaled_data = scaler.transform(input_data)
        print(f"Scaled input data: {scaled_data}")  # Check scaled data
        
        # Make prediction
        prediction = model.predict(scaled_data)
        print(f"Raw prediction result: {prediction}")  # Check raw prediction result
        
        # Translate result to label
        return "COVID-19 Positive" if prediction[0] == 1 else "COVID-19 Negative"
        
    except Exception as e:
        print(f"Error during prediction: {e}")
        traceback.print_exc()
        return "Error with prediction."
