# tests/test_model.py
import pytest
import pandas as pd
from racernix.model.racernix_model import FraudDetector


@pytest.fixture
def sample_data():
    """Fixture to provide a sample dataset"""
    data = pd.DataFrame(
        {
            "amount": [100, 200, 300, 400, 500],
            "location": [1, 2, 1, 3, 2],
            "is_fraud": [0, 0, 1, 0, 1],  # Target column
        }
    )
    return data


def test_model_training(sample_data):
    """Test the model's training process"""
    detector = FraudDetector()
    detector.train(sample_data)

    # Check if the model is trained by ensuring it's not None
    assert detector.model is not None


def test_model_prediction(sample_data):
    """Test if the model can make predictions"""
    detector = FraudDetector()
    detector.train(sample_data)

    predictions = detector.predict(sample_data.drop("is_fraud", axis=1))
    assert len(predictions) == len(sample_data)
