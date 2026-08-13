# Phase 1 Report — Kali Environment Setup & Packet Capture Preparation

## Objective

Set up the Kali Linux development environment for the AI-Based Network Intrusion Detection System and verify live packet capture capability.

---

## Tasks Completed

### System Update

Updated Kali Linux packages.

```bash
sudo apt update && sudo apt upgrade -y
```

### Tool Installation

Installed Python, virtual environment tools, Wireshark, tcpdump, and supporting utilities.

```bash
sudo apt install -y python3 python3-pip python3-venv wireshark tcpdump net-tools tree git
```

### Wireshark Permissions

Added the user to the Wireshark capture group.

```bash
sudo usermod -aG wireshark $USER
```

### Virtual Environment Creation

Created and activated a Python virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

### Python Dependencies Installed

```bash
pip install scapy pandas scikit-learn numpy joblib matplotlib seaborn
pip freeze > requirements.txt
```

### Network Interface Identification

Identified the active network interface:

* **Interface:** `eth0`
* **IP Address:** `10.0.2.15/24`

### Packet Capture Test

Captured live packets using tcpdump.

```bash
sudo tcpdump -i eth0 -c 5
```

Observed:

* DNS A query for `google.com`
* DNS AAAA query for `google.com`
* Reverse DNS PTR query
* ARP request traffic

### Scapy Verification

```bash
python3 -c "from scapy.all import sniff; print('Scapy OK')"
```

Output:

```text
Scapy OK
```

---

# Technical Concepts Learned

* Network interfaces and IP addressing
* DNS traffic analysis
* ARP protocol basics
* Packet sniffing
* Virtual environments
* Python dependency management
* Packet capture permissions in Linux

---

# Outcome

The Kali Linux environment is fully prepared for IDS development. Live network traffic capture has been verified successfully, and the system is ready for implementing the Python packet sniffer in Phase 2.
