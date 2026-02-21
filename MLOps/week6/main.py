import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --- Configuration ---
MODEL_FILE_PATH = os.path.join('models', 'logistic_regression_iris.joblib')

# --- Pydantic Model for Input Validation ---
class IrisFeatures(BaseModel):
    """Defines the input features for a prediction request."""
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# --- FastAPI App Initialization ---
app = FastAPI(
    title="Iris Species Predictor API",
    description="An API to predict the species of an Iris flower based on its features.",
    version="1.0.0"
)

# --- Load Model ---
# Load the trained model from the file.
# This is done once when the application starts.
try:
    model = joblib.load(MODEL_FILE_PATH)
except FileNotFoundError:
    raise RuntimeError(f"Model file not found at {MODEL_FILE_PATH}. Please run train.py first.")

@app.get("/", tags=["General"])
def read_root():
    """Root endpoint to check if the API is running."""
    return {"message": "Welcome to the Iris Species Predictor API!"}

@app.post("/predict", tags=["Prediction"])
def predict_species(features: IrisFeatures):
    """
    Predicts the Iris species from input features.
    """
    # Convert the input features into a pandas DataFrame
    # The model expects a DataFrame with specific column names.
    input_data = pd.DataFrame([features.dict()])

    # Make a prediction
    prediction = model.predict(input_data)

    # Return the prediction
    return {"predicted_species": prediction[0]}