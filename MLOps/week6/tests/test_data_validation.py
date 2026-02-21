import pytest
import pandas as pd
import os

def test_data_file_exists():
    """Test if IRIS data file exists"""
    data_path = 'data/iris.csv'
    assert os.path.exists(data_path), f"Data file not found at {data_path}"

def test_data_loading():
    """Test if IRIS data loads correctly"""
    data_path = 'data/iris.csv'
    df = pd.read_csv(data_path)
    assert df is not None
    assert len(df) > 0

def test_data_shape():
    """Test if data has expected number of rows"""
    data_path = 'data/iris.csv'
    df = pd.read_csv(data_path)
    # IRIS dataset should have 45 samples
    assert len(df) == 45, f"Expected 45 rows, got {len(df)}"

def test_required_columns():
    """Test if all required columns are present"""
    data_path = 'data/iris.csv'
    df = pd.read_csv(data_path)
    
    required_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    for col in required_columns:
        assert col in df.columns, f"Required column '{col}' not found"

def test_no_missing_values():
    """Test for missing values in dataset"""
    data_path = 'data/iris.csv'
    df = pd.read_csv(data_path)
    assert df.isnull().sum().sum() == 0, "Dataset contains missing values"

def test_data_types():
    """Test if feature columns have correct data types"""
    data_path = 'data/iris.csv'
    df = pd.read_csv(data_path)
    
    feature_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    for col in feature_cols:
        assert pd.api.types.is_numeric_dtype(df[col]), f"Column '{col}' should be numeric"
