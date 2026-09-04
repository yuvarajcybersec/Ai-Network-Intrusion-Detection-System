import joblib

from sklearn.ensemble import RandomForestClassifier

from src.detection.realtime_detector import (
    FEATURE_COLUMNS,
    LABEL_MAP,
    MODEL_FILE,
    load_model,
    predict_packet,
)


def test_model_file_exists():
    from pathlib import Path

    assert Path(MODEL_FILE).exists()


def test_model_is_random_forest():
    model = load_model()

    assert isinstance(model, RandomForestClassifier)


def test_model_has_expected_structure():
    model = load_model()

    assert model.n_features_in_ == 6
    assert model.n_estimators == 100
    assert len(FEATURE_COLUMNS) == 6


def test_model_prediction_is_valid():
    model = load_model()

    features = {
        "src_port": 4444,
        "dst_port": 80,
        "packet_length": 512,
        "protocol_encoded": 2,
        "src_ip_present": 1,
        "dst_ip_present": 1,
    }

    prediction = predict_packet(model, features)

    assert prediction in LABEL_MAP.values()
    assert prediction in {"normal", "suspicious"}


def test_model_prediction_probability_is_valid():
    model = load_model()

    features = {
        "src_port": 0,
        "dst_port": 0,
        "packet_length": 64,
        "protocol_encoded": 1,
        "src_ip_present": 1,
        "dst_ip_present": 1,
    }

    probabilities = model.predict_proba(
        [[
            features["src_port"],
            features["dst_port"],
            features["packet_length"],
            features["protocol_encoded"],
            features["src_ip_present"],
            features["dst_ip_present"],
        ]]
    )

    assert probabilities.shape == (1, 2)
    assert all(0 <= probability <= 1 for probability in probabilities[0])
    assert abs(sum(probabilities[0]) - 1.0) < 1e-9
