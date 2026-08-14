# Phase 2 Report — Packet Capture & Feature Extraction

## Objective

Implement a real-time packet capture module and convert captured packets into structured features suitable for machine-learning based intrusion detection.

---

## Tasks Completed

### Packet Sniffer Implementation

Created `src/capture/sniffer.py` using Scapy to capture live traffic from the `eth0` interface.

### Real-Time Packet Capture

Successfully captured ARP, DNS, and ICMP packets generated from local network activity and ping traffic.

### Feature Extraction

Extracted the following fields from each packet:

* Timestamp
* Source IP address
* Destination IP address
* Protocol
* Source port
* Destination port
* Packet length

### CSV Dataset Generation

Saved extracted features into:

`logs/captured_packets.csv`

Example record:

```text id=
```
