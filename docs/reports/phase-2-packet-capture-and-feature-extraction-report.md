# Phase 2 Report — Real-Time Packet Capture & Feature Extraction

## Project

**AI-Based Network Intrusion Detection System**

## Phase

**Phase 2 — Real-Time Packet Capture and Structured Feature Extraction**

## Date

14 August 2026

---

# 1. Objective

The objective of Phase 2 was to implement the core network monitoring component of the intrusion detection system. This phase focused on:

* Capturing live network traffic from the Kali Linux machine.
* Processing packets in real time using Scapy.
* Extracting structured network features from each packet.
* Storing the extracted features in a CSV dataset for future machine-learning analysis.

This phase transforms the project from a simple packet sniffer into a data-generation pipeline suitable for an AI-based IDS.

---

# 2. Environment

* **Operating System:** Kali Linux
* **Python Environment:** Python virtual environment (`venv`)
* **Network Interface:** `eth0`
* **Primary Library:** Scapy

---

# 3. Files Implemented

## Source Code

`src/capture/sniffer.py`

## Dataset Output

`logs/captured_packets.csv`

## Report

`docs/reports/phase-2-packet-capture-and-feature-extraction-report.md`

---

# 4. Implementation Details

## 4.1 Packet Capture Engine

A real-time packet sniffer was implemented using Scapy's `sniff()` function.

```python id=
```
