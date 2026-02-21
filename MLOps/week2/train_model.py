import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
import os
import json

# --- Configuration ---
# !!! UPDATE THIS PATH MANUALLY FOR EACH VERSION !!!
# For V1: os.path.join("data", "v1", "data_v1.csv")
# For V2: os.path.join("data", "v2", "data_v2.csv")
DATA_PATH = os.path.join("data", "v1", "data_v1.csv") # STARTING PATH
MODEL_PATH = "model.joblib"
METRICS_PATH = "metrics.json"
TARGET = 'species'

print(f"Loading data from: {DATA_PATH}")

# --- 1. Data Loading ---
df = pd.read_csv(DATA_PATH)
FEATURES = [col for col in df.columns if col != TARGET]

X = df[FEATURES]
y = df[TARGET]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# --- 2. Model Training ---
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# --- 3. Evaluation and Export ---
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Test Accuracy: {accuracy:.4f}")

# Export Model
joblib.dump(model, MODEL_PATH)
print(f"Model artifact saved to: {MODEL_PATH}")

# Save Metrics (DVC compatible JSON)
with open(METRICS_PATH, "w") as f:
    json.dump({"accuracy": accuracy}, f)
print(f"Metrics saved to {METRICS_PATH}")