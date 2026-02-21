import pytest
import os
from src.evaluate import load_model, evaluate_model
from src.train import train_model

@pytest.fixture(scope="module")
def trained_model():
    """Fixture to ensure model is trained before tests"""
    if not os.path.exists('models/iris_model.pkl'):
        train_model()
    return load_model()

def test_model_file_exists():
    """Test if model file exists"""
    # Train model if it doesn't exist
    if not os.path.exists('models/iris_model.pkl'):
        train_model()
    assert os.path.exists('models/iris_model.pkl'), "Model file not found"

def test_model_loading(trained_model):
    """Test if model loads successfully"""
    assert trained_model is not None
    assert hasattr(trained_model, 'predict')
    assert hasattr(trained_model, 'predict_proba')

def test_model_accuracy():
    """Test if model meets minimum accuracy threshold"""
    accuracy, _, _ = evaluate_model()
    assert accuracy > 0.85, f"Model accuracy {accuracy:.4f} is below threshold of 0.85"

def test_model_predictions(trained_model):
    """Test if model makes valid predictions"""
    import pandas as pd
    from sklearn.model_selection import train_test_split
    
    # Load data
    data_path = 'data/iris.csv'
    df = pd.read_csv(data_path)
    
    feature_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    X = df[feature_cols]
    
    # Make predictions
    predictions = trained_model.predict(X[:10])
    
    assert len(predictions) == 10
    assert all(isinstance(pred, (int, str)) for pred in predictions)

def test_prediction_probabilities(trained_model):
    """Test if model outputs valid probability predictions"""
    import pandas as pd
    
    # Load data
    data_path = 'data/iris.csv'
    df = pd.read_csv(data_path)
    
    feature_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    X = df[feature_cols]
    
    # Get probability predictions
    probas = trained_model.predict_proba(X[:10])
    
    assert probas.shape == (10, 2), "Probability predictions have wrong shape"
    assert (probas >= 0).all() and (probas <= 1).all(), "Probabilities outside [0,1] range"
    assert abs(probas.sum(axis=1) - 1).max() < 1e-6, "Probabilities don't sum to 1"