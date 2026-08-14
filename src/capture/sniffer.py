if __name__ == "__main__":
    start_sniffer(interface="eth0", packet_limit=10)from scapy.all import sniff
from datetime import datetime

packet_count = 0

def process_packet(packet):
    global packet_count
    packet_count += 1

    timestamp = datetime.now().strftime("%H:%M:%S")

    print(f"[{timestamp}] Packet #{packet_count}: {packet.summary()}")

def start_sniffer(interface="eth0", packet_limit=10):
    print("=" * 60)
    print("AI-Based Network Intrusion Detection System")
    print("Phase 2: Packet Capture Module")
    print(f"Interface      : {interface}")
    print(f"Packet limit   : {packet_limit}")
    print("Press Ctrl+C to stop capture early")
    print("=" * 60)

    try:
        sniff(
            iface=interface,
            prn=process_packet,
            count=packet_limit,
            store=False
        )

        print("\nCapture completed successfully.")
        print(f"Total packets captured: {packet_count}")

    except KeyboardInterrupt:
        print("\nCapture stopped by user.")
        print(f"Total packets captured: {packet_count}")

if __name__ == "__main__":
    start_sniffer(interface="eth0", packet_limit=10)
