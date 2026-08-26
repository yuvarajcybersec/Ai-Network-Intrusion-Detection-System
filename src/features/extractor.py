import pandas as pd
from pathlib import Path


INPUT_FILE = "data/processed/labeled_traffic.csv"
OUTPUT_FILE = "data/processed/features.csv"


def extract_features():
    print("=" * 60)
    print("AI-Based Network Intrusion Detection System")
    print("Phase 3: Feature Engineering")
    print("=" * 60)

    df = pd.read_csv(INPUT_FILE)

    # Convert protocol names into numerical values
    protocol_map = {
        "ICMP": 1,
        "TCP": 2,
        "UDP": 3,
        "OTHER": 0
    }

    df["protocol_encoded"] = df["protocol"].map(protocol_map).fillna(0).astype(int)

    # Identify whether source/destination IP information is available
    df["src_ip_present"] = df["src_ip"].notna().astype(int)
    df["dst_ip_present"] = df["dst_ip"].notna().astype(int)

    # Convert labels into numerical values
    df["label_encoded"] = df["label"].map({
        "normal": 0,
        "suspicious": 1
    })

    # Select ML features
    features = df[
        [
            "src_port",
            "dst_port",
            "packet_length",
            "protocol_encoded",
            "src_ip_present",
            "dst_ip_present",
            "label_encoded"
        ]
    ].copy()

    Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)
    features.to_csv(OUTPUT_FILE, index=False)

    print(f"Input dataset  : {INPUT_FILE}")
    print(f"Output dataset : {OUTPUT_FILE}")
    print(f"Rows processed : {len(features)}")
    print(f"Features saved : {len(features.columns)}")
    print("=" * 60)

    print("\nFeature preview:")
    print(features.head())


if __name__ == "__main__":
    extract_features()
