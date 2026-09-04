from pathlib import Path

import pandas as pd

from src.features.extractor import INPUT_FILE, OUTPUT_FILE


def test_input_dataset_exists():
    """Verify that the labeled traffic dataset exists."""

    assert Path(INPUT_FILE).exists(), (
        f"Input dataset not found: {INPUT_FILE}"
    )


def test_protocol_encoding():
    """Verify that protocol names map to expected numeric values."""

    protocol_map = {
        "ICMP": 1,
        "TCP": 2,
        "UDP": 3,
        "OTHER": 0
    }

    assert protocol_map["ICMP"] == 1
    assert protocol_map["TCP"] == 2
    assert protocol_map["UDP"] == 3
    assert protocol_map["OTHER"] == 0


def test_ip_presence_encoding():
    """Verify source and destination IP presence encoding."""

    df = pd.DataFrame({
        "src_ip": ["10.0.3.15", None],
        "dst_ip": ["10.0.3.2", None]
    })

    src_present = df["src_ip"].notna().astype(int)
    dst_present = df["dst_ip"].notna().astype(int)

    assert src_present.tolist() == [1, 0]
    assert dst_present.tolist() == [1, 0]


def test_label_encoding():
    """Verify normal and suspicious labels are encoded correctly."""

    labels = pd.Series([
        "normal",
        "suspicious",
        "normal"
    ])

    encoded = labels.map({
        "normal": 0,
        "suspicious": 1
    })

    assert encoded.tolist() == [0, 1, 0]


def test_feature_dataset_exists():
    """Verify that the generated feature dataset exists."""

    assert Path(OUTPUT_FILE).exists(), (
        f"Feature dataset not found: {OUTPUT_FILE}"
    )


def test_feature_dataset_columns():
    """Verify that the feature dataset has the expected columns."""

    output_path = Path(OUTPUT_FILE)

    assert output_path.exists(), (
        f"Feature dataset not found: {OUTPUT_FILE}"
    )

    df = pd.read_csv(output_path)

    expected_columns = {
        "src_port",
        "dst_port",
        "packet_length",
        "protocol_encoded",
        "src_ip_present",
        "dst_ip_present",
        "label_encoded"
    }

    assert set(df.columns) == expected_columns


def test_feature_dataset_is_not_empty():
    """Verify that the feature dataset contains records."""

    df = pd.read_csv(OUTPUT_FILE)

    assert len(df) > 0


def test_feature_dataset_has_no_missing_values():
    """Verify that engineered features contain no missing values."""

    df = pd.read_csv(OUTPUT_FILE)

    assert not df.isnull().values.any()
