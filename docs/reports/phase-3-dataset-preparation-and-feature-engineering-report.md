# Phase 3 — Dataset Preparation and Feature Engineering Report

## AI-Based Network Intrusion Detection System

---

## 1. Phase Overview

Phase 3 focuses on preparing network traffic data for machine-learning-based intrusion detection.

The main objectives of this phase were:

- Capture and label network traffic.
- Separate normal and suspicious traffic.
- Generate suspicious traffic using a controlled Nmap scan in the isolated lab environment.
- Validate the collected datasets.
- Combine the traffic into a single labeled dataset.
- Convert raw categorical information into numerical machine-learning features.
- Validate the engineered feature dataset.

This phase prepares the data pipeline required for the machine-learning stage.

---

## 2. Lab Environment

The project was developed and tested in Kali Linux using a virtualized laboratory environment.

### Network Configuration

Kali Linux network interface:

```text
Interface : eth0
Kali IP  : 10.0.2.15/24
Gateway  : 10.0.2.2

ping -c 4 192.168.56.101
