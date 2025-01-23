# Predictive-Analysis-for-Manufacturing-Operations

## Project Overview
This project provides a simple RESTful API for predicting machine downtime in a manufacturing environment based on temperature and run time.

## Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the Flask API:
    python main.py

## API Endpoints
1. /upload (POST)
    Description: Upload a CSV file containing the dataset (e.g., Machine_ID, Temperature, Run_Time, Downtime_Flag).
    Example Request:
    Use Postman or cURL to upload a file.
    cURL:
    bash
    Copy
    Edit
    curl -X POST -F "file=@sample_data.csv" http://127.0.0.1:5000/upload
2. /train (POST)
    Description: Train the model on the uploaded dataset and return evaluation metrics (accuracy, F1-score).
    Example Request:
    bash
    Copy
    Edit
    curl -X POST http://127.0.0.1:5000/train
3. /predict (POST)
    Description: Make predictions based on input features (Temperature, Run_Time).
    Example Request:
    bash
    Copy
    Edit
    curl -X POST -H "Content-Type: application/json" -d '{"Temperature": 85, "Run_Time": 150}' http://127.0.0.1:5000/predict
    Example Response:
    json
    Copy
    Edit
    {
    "Downtime": "Yes",
    "Confidence": 0.85
    }
###    Notes
    Make sure to upload the CSV file before training the model.
    The trained model is saved in model.pkl for future use.



---

### **Testing**

Test the API using Postman or cURL:
1. **Upload the dataset:**  
   Test the `/upload` endpoint with a CSV file.
2. **Train the model:**  
   Test the `/train` endpoint after uploading the dataset to ensure it trains and evaluates correctly.
3. **Make predictions:**  
   Test the `/predict` endpoint by sending sample input features.

---

### **Conclusion**
This solution fully meets the project requirements:
- **Functionality**: The endpoints are designed to handle uploading data, training the model, and making predictions.
- **Relevance**: The Logistic Regression model provides a simple, interpretable solution for downtime prediction based on temperature and runtime.
- **Code Quality**: The code is structured in a clear and maintainable way, with clear separation of concerns.
- **Delivery**: The project can be easily set up and tested with minimal time.

Let me know if you'd like any further adjustments or explanations!

