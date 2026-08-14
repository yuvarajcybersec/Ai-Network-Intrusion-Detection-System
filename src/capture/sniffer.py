from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
import csv
import os

packet_count = 0
csv_file = "logs/captured_packets.csv"

# Create logs directory if it does not exist
os.makedirs("logs", exist_ok=True)

# Create CSV file with header if it does not exist
if not os.path.exists(csv_file):
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "timestamp",
            "src_ip",
            "dst_ip",
            "protocol",
            "src_port",
            "dst_port",
            "packet_length"
        ])

def extract_features(packet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    src_ip = "N/A"
    dst_ip = "N/A"
    protocol = "OTHER"
    src_port = 0
    dst_port = 0

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

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

    packet_length = len(packet)

    return [
        timestamp,
        src_ip,
        dst_ip,
        protocol,
        src_port,
        dst_port,
        packet_length
    ]

def process_packet(packet):
    global packet_count
    packet_count += 1

    features = extract_features(packet)

    # Save features to CSV
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(features)

    print(
        f"[{features[0]}] "
        f"{features[1]} -> {features[2]} "
        f"{features[3]} "
        f"len={features[6]}"
    )

def start_sniffer(interface="eth0", packet_limit=10):
    print("=" * 60)
    print("AI-Based Network Intrusion Detection System")
    print("Phase 2 Part B: Feature Extraction Module")
    print(f"Interface    : {interface}")
    print(f"Packet limit : {packet_limit}")
    print(f"CSV Output   : {csv_file}")
    print("=" * 60)

    sniff(
        iface=interface,
        prn=process_packet,
        count=packet_limit,
        store=False
    )

    print("\nCapture completed successfully.")
    print(f"Total packets captured: {packet_count}")

if __name__ == "__main__":
    start_sniffer(interface="eth0", packet_limit=10)
