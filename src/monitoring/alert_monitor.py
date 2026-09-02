import re
from collections import Counter
from pathlib import Path


ALERT_LOG = "logs/alerts.log"


ALERT_PATTERN = re.compile(
    r"\[ALERT\]\s+"
    r"(?P<timestamp>[^|]+)\s+\|\s+"
    r"Prediction=(?P<prediction>[^|]+)\s+\|\s+"
    r"(?P<src_ip>[^:|]+):(?P<src_port>\d+)\s+->\s+"
    r"(?P<dst_ip>[^:|]+):(?P<dst_port>\d+)\s+\|\s+"
    r"Protocol=(?P<protocol>[^|]+)\s+\|\s+"
    r"Length=(?P<length>\d+)"
)


def load_alerts():
    """Load and parse alert entries from the alert log."""

    log_path = Path(ALERT_LOG)

    if not log_path.exists():
        raise FileNotFoundError(
            f"Alert log not found: {ALERT_LOG}"
        )

    alerts = []

    with open(log_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            match = ALERT_PATTERN.match(line)

            if not match:
                continue

            data = match.groupdict()

            alerts.append(
                {
                    "timestamp": data["timestamp"].strip(),
                    "prediction": data["prediction"].strip(),
                    "src_ip": data["src_ip"].strip(),
                    "src_port": int(data["src_port"]),
                    "dst_ip": data["dst_ip"].strip(),
                    "dst_port": int(data["dst_port"]),
                    "protocol": data["protocol"].strip(),
                    "length": int(data["length"])
                }
            )

    return alerts


def calculate_statistics(alerts):
    """Calculate summary statistics from parsed alerts."""

    if not alerts:
        return {
            "total_alerts": 0,
            "protocol_distribution": {},
            "source_distribution": {},
            "destination_distribution": {},
            "average_packet_length": 0,
            "minimum_packet_length": 0,
            "maximum_packet_length": 0
        }

    protocol_distribution = Counter(
        alert["protocol"]
        for alert in alerts
    )

    source_distribution = Counter(
        alert["src_ip"]
        for alert in alerts
    )

    destination_distribution = Counter(
        alert["dst_ip"]
        for alert in alerts
    )

    packet_lengths = [
        alert["length"]
        for alert in alerts
    ]

    return {
        "total_alerts": len(alerts),
        "protocol_distribution": dict(protocol_distribution),
        "source_distribution": dict(source_distribution),
        "destination_distribution": dict(destination_distribution),
        "average_packet_length": sum(packet_lengths) / len(packet_lengths),
        "minimum_packet_length": min(packet_lengths),
        "maximum_packet_length": max(packet_lengths)
    }


def display_statistics(statistics):
    """Display alert monitoring statistics."""

    print("=" * 60)
    print("AI-Based Network Intrusion Detection System")
    print("Phase 6: Alert Monitoring & Detection Statistics")
    print("=" * 60)

    print(f"Total alerts       : {statistics['total_alerts']}")

    print("\nProtocol Distribution:")
    for protocol, count in statistics["protocol_distribution"].items():
        print(f"  {protocol:<10}: {count}")

    print("\nSource IP Distribution:")
    for source, count in statistics["source_distribution"].items():
        print(f"  {source:<20}: {count}")

    print("\nDestination IP Distribution:")
    for destination, count in statistics["destination_distribution"].items():
        print(f"  {destination:<20}: {count}")

    print("\nPacket Length Statistics:")
    print(
        f"  Average : "
        f"{statistics['average_packet_length']:.2f} bytes"
    )
    print(
        f"  Minimum : "
        f"{statistics['minimum_packet_length']} bytes"
    )
    print(
        f"  Maximum : "
        f"{statistics['maximum_packet_length']} bytes"
    )

    print("=" * 60)


def main():
    """Run the Phase 6 alert monitoring module."""

    alerts = load_alerts()

    statistics = calculate_statistics(alerts)

    display_statistics(statistics)


if __name__ == "__main__":
    main()
