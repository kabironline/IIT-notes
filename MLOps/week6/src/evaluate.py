import mlflow
import mlflow.pyfunc
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.preprocessing import LabelEncoder

# The MLFlow tracking URI will be picked up from the MLFLOW_TRACKING_URI environment variable.

print(f"MLFlow Tracking URI: {mlflow.get_tracking_uri()}")

def evaluate_model():
    # 1. Fetch the latest/best model from MLFlow Model Registry
    # You can specify a stage (e.g., "Production", "Staging") or "latest" version
    model_name = "IrisModel"
    # For simplicity, we'll fetch the latest version.
    # In a real scenario, you might fetch a model in a specific stage like "Production"
    model_uri = f"models:/{model_name}/latest"

    print(f"Fetching model from MLFlow Model Registry: {model_uri}")
    model = mlflow.pyfunc.load_model(model_uri)
    print("Model loaded successfully.")

    # 2. Prepare Evaluation Data from iris.csv
    data_path = "data/iris.csv"
    print(f"Loading evaluation data from {data_path}")
    df = pd.read_csv(data_path)

    X = df.drop("species", axis=1)
    y_raw = df["species"]

    le = LabelEncoder()
    y = le.fit_transform(y_raw)

    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Evaluate the model
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"F1 Score (Weighted): {f1_score(y_test, y_pred, average='weighted'):.4f}")

if __name__ == "__main__":
    evaluate_model()