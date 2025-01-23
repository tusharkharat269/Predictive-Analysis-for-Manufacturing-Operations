from flask import Flask, request, jsonify
import pandas as pd
from model import train_model, predict
import os

app = Flask(__name__)
data = None

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Manufacturing Predictive Analysis API!"

@app.route('/upload', methods=['POST'])
def upload_data():
    global data
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and file.filename.endswith('.csv'):
        data = pd.read_csv(file)
        return jsonify({"message": "Data uploaded successfully"}), 200
    else:
        return jsonify({"error": "Invalid file format"}), 400

@app.route('/train', methods=['POST'])
def train():
    if data is None:
        return jsonify({"error": "No data uploaded"}), 400
    
    accuracy, f1 = train_model(data)
    return jsonify({"accuracy": accuracy, "f1_score": f1}), 200

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    if data is None:
        return jsonify({"error": "No model trained yet"}), 400

    input_data = request.json
    if "Temperature" not in input_data or "Run_Time" not in input_data:
        return jsonify({"error": "Missing required features"}), 400
    
    prediction, confidence = predict(input_data)
    result = "Yes" if prediction == 1 else "No"
    
    return jsonify({"Downtime": result, "Confidence": confidence}), 200

if __name__ == '__main__':
    app.run(debug=True)
