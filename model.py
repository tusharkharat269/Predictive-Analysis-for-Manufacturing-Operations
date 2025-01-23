import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import joblib

def train_model(data):
    X = data[["Temperature", "Run_Time"]]  # Features
    y = data["Downtime_Flag"]  # Target
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    joblib.dump(model, 'model.pkl')
    
    return accuracy, f1

def predict(data):
    model = joblib.load('model.pkl')
    prediction = model.predict([[data["Temperature"], data["Run_Time"]]])
    confidence = max(model.predict_proba([[data["Temperature"], data["Run_Time"]]])[0])
    
    return prediction[0], confidence
