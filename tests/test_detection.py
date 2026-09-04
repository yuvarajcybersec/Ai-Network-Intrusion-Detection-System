from scapy.all import IP, TCP, UDP, ICMP, Raw

from src.detection.realtime_detector import (
    FEATURE_COLUMNS,
    extract_packet_features,
    load_model,
    predict_packet,
)


def test_icmp_packet_feature_extraction():
    packet = IP(
        src="10.0.3.15",
        dst="10.0.3.2"
    ) / ICMP() / Raw(load=b"test")

    features, packet_info = extract_packet_features(packet)

    assert features["src_port"] == 0
    assert features["dst_port"] == 0
    assert features["protocol_encoded"] == 1
    assert features["src_ip_present"] == 1
    assert features["dst_ip_present"] == 1
    assert features["packet_length"] == len(packet)

    assert packet_info["src_ip"] == "10.0.3.15"
    assert packet_info["dst_ip"] == "10.0.3.2"
    assert packet_info["protocol"] == "ICMP"


def test_tcp_packet_feature_extraction():
    packet = (
        IP(src="10.0.3.15", dst="10.0.3.2")
        / TCP(sport=4444, dport=80)
    )

    features, packet_info = extract_packet_features(packet)

    assert features["src_port"] == 4444
    assert features["dst_port"] == 80
    assert features["protocol_encoded"] == 2
    assert features["src_ip_present"] == 1
    assert features["dst_ip_present"] == 1

    assert packet_info["protocol"] == "TCP"
    assert packet_info["src_port"] == 4444
    assert packet_info["dst_port"] == 80


def test_udp_packet_feature_extraction():
    packet = (
        IP(src="10.0.3.15", dst="10.0.3.2")
        / UDP(sport=5353, dport=53)
    )

    features, packet_info = extract_packet_features(packet)

    assert features["src_port"] == 5353
    assert features["dst_port"] == 53
    assert features["protocol_encoded"] == 3
    assert packet_info["protocol"] == "UDP"


def test_non_ip_packet_feature_extraction():
    packet = Raw(load=b"test-packet")

    features, packet_info = extract_packet_features(packet)

    assert features["src_port"] == 0
    assert features["dst_port"] == 0
    assert features["protocol_encoded"] == 0
    assert features["src_ip_present"] == 0
    assert features["dst_ip_present"] == 0

    assert packet_info["src_ip"] == "N/A"
    assert packet_info["dst_ip"] == "N/A"
    assert packet_info["protocol"] == "OTHER"


def test_model_loading():
    model = load_model()

    assert model is not None
    assert type(model).__name__ == "RandomForestClassifier"
    assert model.n_features_in_ == len(FEATURE_COLUMNS)
    assert model.n_estimators == 100


def test_model_prediction_returns_valid_label():
    model = load_model()

    features = {
        "src_port": 0,
        "dst_port": 0,
        "packet_length": 64,
        "protocol_encoded": 1,
        "src_ip_present": 1,
        "dst_ip_present": 1,
    }

    prediction = predict_packet(model, features)

    assert prediction in {"normal", "suspicious"}
