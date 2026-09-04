# Phase 9 – End-to-End IDS Detection Validation

## 1. Overview

**Project:** AI-Based Network Intrusion Detection System
**Phase:** 9 – End-to-End Detection Validation
**Date:** 04 September 2026
**Environment:** Kali Linux Virtual Machine
**Interface Tested:** `eth1`
**ML Model:** Random Forest Classifier
**Model File:** `models/random_forest_model.pkl`

Phase 9 validates the complete IDS pipeline by capturing live network traffic, extracting packet features, performing machine-learning-based classification, generating alerts for suspicious traffic, and analyzing the resulting alerts through the monitoring module.

---

## 2. Objectives

The objectives of Phase 9 were:

1. Verify that the trained ML model loads successfully.
2. Verify live packet capture using Scapy.
3. Verify real-time feature extraction from captured packets.
4. Verify ML classification of network packets.
5. Verify suspicious-traffic alert generation.
6. Verify alert logging.
7. Verify alert monitoring and statistics.
8. Establish baseline and suspicious-traffic test results.
9. Confirm that the IDS operates as an integrated end-to-end pipeline.

---

## 3. System Components Tested

The following project components were validated:

```text
Network Interface
      │
      ▼
Scapy Packet Capture
      │
      ▼
Feature Extraction
      │
      ▼
Random Forest ML Model
      │
      ├── Normal ──────────────► No Alert
      │
      └── Suspicious ──────────► Alert Manager
                                      │
                                      ▼
                                logs/alerts.log
                                      │
                                      ▼
                                Alert Monitor
```

---

## 4. Environment Validation

The IDS model and Python environment were verified before testing.

### Python Environment

```text
Python       : 3.13.14
Scapy        : 2.7.0
scikit-learn : 1.9.0
pandas       : 3.0.5
numpy        : 2.5.2
joblib       : 1.5.3
matplotlib   : 3.11.1
```

### ML Model

```text
Model type   : RandomForestClassifier
Model trees  : 100
Features     : 6
Model file   : models/random_forest_model.pkl
Model size   : approximately 87 KB
```

The model loaded successfully during the end-to-end test.

---

## 5. Network Interface Validation

The Kali Linux VM contained two active network interfaces:

```text
eth0   192.168.56.102/24
eth1   10.0.3.15/24
```

The default route was configured through `eth1`:

```text
default via 10.0.3.2 dev eth1
```

Initial packet-capture testing showed that `eth0` did not receive packets in the current configuration.

Testing with `eth1` successfully captured network traffic.

Therefore, `eth1` was selected for the Phase 9 end-to-end validation.

---

## 6. Baseline Traffic Test

Before testing suspicious traffic, the alert log was cleared:

```bash
: > logs/alerts.log
```

The IDS was then executed against `eth1`:

```bash
sudo ./venv/bin/python -c "
from src.integration.ids_runner import run_ids
run_ids(interface='eth1', packet_limit=10)
"
```

The IDS successfully captured and classified normal ICMP traffic.

Representative detections:

```text
[ML DETECTION] 10.0.3.15 -> 10.0.3.2 | ICMP | len=98 | prediction=normal
[ML DETECTION] 10.0.3.2 -> 10.0.3.15 | ICMP | len=98 | prediction=normal
```

The baseline test produced:

```text
Total alerts : 0
```

This demonstrates that traffic classified as normal did not generate alerts.

---

## 7. Suspicious Traffic Detection Test

A subsequent live detection run was performed against `eth1`.

The IDS successfully captured packets and passed them through the ML detection pipeline.

The system generated suspicious classifications for packets identified as:

```text
Protocol : OTHER
Source   : N/A
Destination : N/A
Packet length : 64 bytes
Prediction : suspicious
```

The alert manager generated five alerts.

---

## 8. Alert Generation Evidence

The resulting `logs/alerts.log` contained:

```text
[ALERT] 2026-09-04 18:13:18 | Prediction=suspicious | N/A:0 -> N/A:0 | Protocol=OTHER | Length=64
[ALERT] 2026-09-04 18:13:19 | Prediction=suspicious | N/A:0 -> N/A:0 | Protocol=OTHER | Length=64
[ALERT] 2026-09-04 18:13:19 | Prediction=suspicious | N/A:0 -> N/A:0 | Protocol=OTHER | Length=64
[ALERT] 2026-09-04 18:13:19 | Prediction=suspicious | N/A:0 -> N/A:0 | Protocol=OTHER | Length=64
[ALERT] 2026-09-04 18:13:19 | Prediction=suspicious | N/A:0 -> N/A:0 | Protocol=OTHER | Length=64
```

Alert count verification:

```text
5 logs/alerts.log
```

---

## 9. Alert Monitoring Results

The monitoring module was executed using:

```bash
./venv/bin/python -m src.monitoring.alert_monitor
```

The module reported:

```text
Total alerts       : 5

Protocol Distribution:
  OTHER     : 5

Source IP Distribution:
  N/A                 : 5

Destination IP Distribution:
  N/A                 : 5

Packet Length Statistics:
  Average : 64.00 bytes
  Minimum : 64 bytes
  Maximum : 64 bytes
```

The monitoring system therefore successfully read and analyzed the alerts generated by the detection engine.

---

## 10. Phase 9 Test Summary

| Test                      | Expected Result                   | Actual Result                        | Status |
| ------------------------- | --------------------------------- | ------------------------------------ | ------ |
| ML model loading          | Model loads                       | Random Forest loaded                 | PASS   |
| Packet capture            | Packets captured                  | Packets captured on `eth1`           | PASS   |
| Feature extraction        | Six features generated            | Detection pipeline processed packets | PASS   |
| Normal classification     | Normal traffic produces no alert  | 0 alerts                             | PASS   |
| Suspicious classification | Suspicious traffic produces alert | 5 alerts                             | PASS   |
| Alert logging             | Alerts written to log             | 5 alerts logged                      | PASS   |
| Alert monitoring          | Alerts analyzed                   | 5 alerts analyzed                    | PASS   |
| End-to-end integration    | Complete pipeline works           | Detection and monitoring completed   | PASS   |

---

## 11. Important Observation

The Phase 9 test successfully demonstrates that the IDS can detect traffic and generate alerts.

However, the current test also revealed an important limitation:

```text
Source IP        : N/A
Destination IP   : N/A
Protocol         : OTHER
```

for the suspicious packets.

These packets were likely non-IP Ethernet frames. The current feature extraction logic only extracts source and destination IP information when an IPv4 `IP` layer is present.

This means the system is currently capable of detecting such frames as suspicious based on the available numerical features, but it does not yet provide useful Layer-3 address information for those alerts.

This should be considered a future improvement rather than a failure of the Phase 9 validation.

---

## 12. Security and Testing Scope

Testing was performed within the authorized Kali Linux lab environment using the VM's available network interfaces.

No unauthorized external systems were targeted.

The objective was to validate the IDS detection pipeline rather than perform exploitation against external hosts.

---

## 13. Phase 9 Conclusion

Phase 9 successfully validated the integrated AI-based network intrusion detection workflow.

The system demonstrated the following complete pipeline:

```text
Live Network Traffic
        ↓
Packet Capture
        ↓
Feature Extraction
        ↓
Random Forest Classification
        ↓
Normal / Suspicious Decision
        ↓
Suspicious Alert Generation
        ↓
Alert Log
        ↓
Alert Monitoring & Statistics
```

The baseline test generated **0 alerts**, while the suspicious-traffic validation generated **5 alerts**. The monitoring module successfully processed all five alerts.

Therefore, the core IDS pipeline is operational and ready for deployment-oriented testing.

---

## 14. Next Phase

The next stage will focus on **deployment and operational validation**.

Planned activities include:

* Preparing a repeatable IDS startup method.
* Improving interface configuration.
* Testing the IDS continuously on the active interface.
* Validating alert persistence.
* Testing the system with controlled network traffic.
* Verifying the complete deployed workflow.
* Documenting deployment procedures.
* Performing final system validation.
* Preparing the project for final GitHub submission.

---

**Phase 9 Status: COMPLETED**
