import joblib
import pandas as pd

from pathlib import Path
from scapy.all import sniff, IP, TCP, UDP, ICMP

from src.alerts.alert_manager import generate_alert


MODEL_FILE = "models/random_forest_model.pkl"

FEATURE_COLUMNS = [
    "src_port",
    "dst_port",
    "packet_length",
    "protocol_encoded",
    "src_ip_present",
    "dst_ip_present"
]

LABEL_MAP = {
    0: "normal",
    1: "suspicious"
}


def load_model():
    """Load the trained Random Forest model."""

    if not Path(MODEL_FILE).exists():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_FILE}"
        )

    return joblib.load(MODEL_FILE)


def extract_packet_features(packet):
    """
    Extract the six features used by the Phase 4 ML model
    from a live network packet.
    """

    src_ip = "N/A"
    dst_ip = "N/A"

    src_port = 0
    dst_port = 0

    protocol = "OTHER"

    src_ip_present = 0
    dst_ip_present = 0

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        src_ip_present = 1
        dst_ip_present = 1

        if packet.haslayer(TCP):
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        elif packet.haslayer(UDP):
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        elif packet.haslayer(ICMP):
            protocol = "ICMP"

    protocol_map = {
        "OTHER": 0,
        "ICMP": 1,
        "TCP": 2,
        "UDP": 3
    }

    protocol_encoded = protocol_map.get(protocol, 0)

    packet_length = len(packet)

    features = {
        "src_port": src_port,
        "dst_port": dst_port,
        "packet_length": packet_length,
        "protocol_encoded": protocol_encoded,
        "src_ip_present": src_ip_present,
        "dst_ip_present": dst_ip_present
    }

    return features, {
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "protocol": protocol,
        "src_port": src_port,
        "dst_port": dst_port,
        "packet_length": packet_length
    }


def predict_packet(model, features):
    """Predict whether a packet is normal or suspicious."""

    dataframe = pd.DataFrame(
        [features],
        columns=FEATURE_COLUMNS
    )

    prediction = model.predict(dataframe)[0]

    return LABEL_MAP.get(
        int(prediction),
        "unknown"
    )


def process_packet(packet, model):
    """Process one captured packet through the ML pipeline."""

    features, packet_info = extract_packet_features(packet)

    prediction = predict_packet(
        model,
        features
    )

    print(
        f"[ML DETECTION] "
        f"{packet_info['src_ip']} -> "
        f"{packet_info['dst_ip']} | "
        f"{packet_info['protocol']} | "
        f"len={packet_info['packet_length']} | "
        f"prediction={prediction}"
    )

    generate_alert(
        src_ip=packet_info["src_ip"],
        dst_ip=packet_info["dst_ip"],
        protocol=packet_info["protocol"],
        src_port=packet_info["src_port"],
        dst_port=packet_info["dst_port"],
        packet_length=packet_info["packet_length"],
        prediction=prediction
    )


def start_realtime_detection(
    interface="eth0",
    packet_limit=10
):
    """Start real-time ML-based network traffic detection."""

    print("=" * 60)
    print("AI-Based Network Intrusion Detection System")
    print("Phase 5: Real-Time ML Traffic Detection")
    print("=" * 60)
    print(f"Interface    : {interface}")
    print(f"Packet limit : {packet_limit}")
    print(f"Model        : {MODEL_FILE}")
    print("=" * 60)

    model = load_model()

    print("\nModel loaded successfully.")
    print(f"Model type   : {type(model).__name__}")
    print(f"Features     : {model.n_features_in_}")

    print("\nStarting packet capture...")
    print("Generate some network traffic to test detection.\n")

    sniff(
        iface=interface,
        prn=lambda packet: process_packet(packet, model),
        count=packet_limit,
        store=False
    )

    print("\nReal-time detection completed successfully.")


if __name__ == "__main__":
    start_realtime_detection(
        interface="eth0",
        packet_limit=10
    )
