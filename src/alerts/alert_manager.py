from datetime import datetime
from pathlib import Path


ALERT_LOG = "logs/alerts.log"


def generate_alert(
    src_ip,
    dst_ip,
    protocol,
    src_port,
    dst_port,
    packet_length,
    prediction
):
    """
    Generate an alert when suspicious traffic is detected.
    """

    if prediction != "suspicious":
        return

    Path(ALERT_LOG).parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    alert = (
        f"[ALERT] {timestamp} | "
        f"Prediction=suspicious | "
        f"{src_ip}:{src_port} -> "
        f"{dst_ip}:{dst_port} | "
        f"Protocol={protocol} | "
        f"Length={packet_length}"
    )

    print("\n" + "!" * 60)
    print("INTRUSION ALERT")
    print("!" * 60)
    print(alert)
    print("!" * 60)

    with open(ALERT_LOG, "a") as file:
        file.write(alert + "\n")


def test_alert():
    """Test suspicious traffic alert generation."""

    print("=" * 60)
    print("AI-Based Network Intrusion Detection System")
    print("Phase 5: Alert Manager Test")
    print("=" * 60)

    generate_alert(
        src_ip="192.168.1.100",
        dst_ip="192.168.1.10",
        protocol="TCP",
        src_port=4444,
        dst_port=80,
        packet_length=512,
        prediction="suspicious"
    )

    print("\nAlert test completed successfully.")
    print(f"Alert log: {ALERT_LOG}")
    print("=" * 60)


if __name__ == "__main__":
    test_alert()
