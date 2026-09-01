# Phase 5 – Real-Time ML-Based Traffic Detection and Alerting

## 1. Overview

Phase 5 integrates the trained Random Forest machine-learning model from Phase 4 with the network packet capture pipeline.

The objective is to perform real-time network traffic classification and generate alerts whenever the machine-learning model predicts suspicious traffic.

The Phase 5 pipeline is:

Network Interface
        |
        v
Packet Capture
        |
        v
Feature Extraction
        |
        v
Random Forest Model
        |
        v
Traffic Prediction
     /        \
 normal    suspicious
              |
              v
        Alert Manager
              |
              v
       logs/alerts.log

---

## 2. Phase Objectives

The objectives of Phase 5 were:

- Load the trained Random Forest model.
- Capture network packets in real time.
- Extract the same six features used during model training.
- Convert captured packets into machine-learning input.
- Predict whether traffic is normal or suspicious.
- Display real-time detection results.
- Generate alerts for suspicious predictions.
- Store generated alerts in a persistent log file.
- Verify the complete detection and alerting pipeline.

---

## 3. Model Used

The model generated during Phase 4 was used:

models/random_forest_model.pkl

Model type:

RandomForestClassifier

Model configuration:

- Trees: 100
- Features: 6

The six input features are:

1. src_port
2. dst_port
3. packet_length
4. protocol_encoded
5. src_ip_present
6. dst_ip_present

---

## 4. Real-Time Detection Module

The real-time detection module is located at:

src/detection/realtime_detector.py

The module performs the following operations:

1. Loads the trained machine-learning model.
2. Captures packets from the eth0 interface.
3. Extracts packet-level features.
4. Converts the extracted features into the required ML format.
5. Sends the feature vector to the Random Forest model.
6. Converts the numerical prediction into a human-readable label.
7. Displays the prediction in real time.
8. Sends suspicious predictions to the alert manager.

---

## 5. Packet Feature Extraction Test

A Scapy TCP packet was created to verify that packet features could be extracted correctly.

Test packet:

- Source IP: 10.0.2.15
- Destination IP: 10.0.2.2
- Source Port: 4444
- Destination Port: 80
- Protocol: TCP
- Packet length: 40

Command:

python -c "from scapy.all import IP, TCP; from src.detection.realtime_detector import extract_packet_features; p=IP(src='10.0.2.15',dst='10.0.2.2')/TCP(sport=4444,dport=80); print(extract_packet_features(p))"

Result:

- src_port: 4444
- dst_port: 80
- packet_length: 40
- protocol_encoded: 2
- src_ip_present: 1
- dst_ip_present: 1

The feature extraction test completed successfully.

---

## 6. Individual ML Prediction Test

The extracted packet features were passed directly to the trained Random Forest model.

Result:

Prediction: suspicious

This confirmed that the trained model successfully accepts the feature representation produced by the real-time detection module.

---

## 7. Alert Manager

The alert manager is located at:

src/alerts/alert_manager.py

A test alert was successfully generated:

[ALERT] 2026-09-01 19:57:06 | Prediction=suspicious | 192.168.1.100:4444 -> 192.168.1.10:80 | Protocol=TCP | Length=512

The alert was written to:

logs/alerts.log

---

## 8. Real-Time Detection Test

The complete detection system was executed using:

sudo ./venv/bin/python -m src.detection.realtime_detector

The model loaded successfully:

Model type: RandomForestClassifier
Features: 6

Packet capture was performed on:

Interface: eth0
Packet limit: 10

The system successfully classified both normal and suspicious traffic.

Example normal traffic:

[ML DETECTION] 10.0.2.15 -> 192.168.1.1 | UDP | len=71 | prediction=normal

Example suspicious traffic:

[ML DETECTION] 104.20.23.154 -> 10.0.2.15 | TCP | len=60 | prediction=suspicious

The suspicious prediction triggered the alert manager:

[ALERT] 2026-09-01 20:05:28 | Prediction=suspicious | 104.20.23.154:80 -> 10.0.2.15:54180 | Protocol=TCP | Length=60

Another suspicious packet was detected:

[ML DETECTION] 10.0.2.15 -> 104.20.23.154 | TCP | len=54 | prediction=suspicious

This also generated an alert:

[ALERT] 2026-09-01 20:05:28 | Prediction=suspicious | 10.0.2.15:54180 -> 104.20.23.154:80 | Protocol=TCP | Length=54

The real-time detection process completed successfully.

---

## 9. Alert Log Verification

The generated alerts were verified using:

cat logs/alerts.log

The log contained multiple alerts generated during Phase 5 testing, including TCP and OTHER traffic classifications.

This confirms that suspicious predictions are passed from the detection module to the alert manager and persisted to disk.

---

## 10. Validation Tests

| Test | Result |
|---|---|
| Python syntax compilation | PASS |
| Alert manager import | PASS |
| Packet feature extraction | PASS |
| ML model loading | PASS |
| Individual packet prediction | PASS |
| Real-time packet capture | PASS |
| Normal traffic classification | PASS |
| Suspicious traffic classification | PASS |
| Alert generation | PASS |
| Alert log persistence | PASS |

---

## 11. Important Observation

The Phase 4 model was trained using a relatively small dataset containing 30 samples.

Therefore, the successful Phase 5 predictions demonstrate that the technical detection pipeline is functioning, but they should not be interpreted as proof of production-level detection accuracy.

A larger and more representative dataset should be used in future phases to improve model generalization and reduce potential false positives.

---

## 12. Phase 5 Outcome

Phase 5 successfully integrated machine learning into the network monitoring pipeline.

The system can now:

Capture packets
        |
        v
Extract features
        |
        v
Run ML prediction
        |
        v
Classify traffic
        |
        v
Detect suspicious traffic
        |
        v
Generate intrusion alert
        |
        v
Store alert in log

This establishes the core real-time detection and alerting capability of the AI-Based Network Intrusion Detection System.

---

## 13. Files Involved

- src/detection/realtime_detector.py
- src/alerts/alert_manager.py
- models/random_forest_model.pkl
- logs/alerts.log
- data/processed/features.csv
- docs/reports/phase-5-real-time-ml-detection-and-alerting-report.md

---

## 14. Conclusion

Phase 5 was completed successfully.

The trained Random Forest model from Phase 4 was integrated with real-time packet capture. Packets were converted into the required feature representation, classified by the ML model, and suspicious predictions were forwarded to the alert manager.

The complete pipeline was tested successfully on the Kali Linux environment using the eth0 network interface.

The system is now ready for the next phase of development.
