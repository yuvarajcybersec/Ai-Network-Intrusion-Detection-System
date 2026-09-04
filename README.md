# AI-Based Network Intrusion Detection System

A machine-learning-based Network Intrusion Detection System (NIDS) developed in Python to capture live network traffic, extract packet-level features, classify traffic using a trained Random Forest model, and generate alerts for suspicious activity.

The project was developed and validated progressively from network setup through end-to-end detection, performance evaluation, and clean-environment deployment validation.

---

## Project Overview

Traditional intrusion detection systems often rely heavily on predefined signatures and rules. This project explores a machine-learning approach in which network traffic is converted into structured features and classified as **normal** or **suspicious**.

The system provides an end-to-end pipeline:

```text
Network Traffic
      │
      ▼
Packet Capture
      │
      ▼
Feature Extraction
      │
      ▼
Dataset Preparation
      │
      ▼
Machine Learning Model
      │
      ▼
Real-Time Detection
      │
      ▼
Alert Generation
      │
      ▼
Alert Monitoring & Statistics
```

---

## Key Features

* Live packet capture using Scapy
* Network packet feature extraction
* Labeled traffic dataset preparation
* Feature engineering for machine-learning classification
* Random Forest intrusion detection model
* Real-time packet classification
* Suspicious traffic alert generation
* Alert logging
* Detection statistics and monitoring
* Model performance evaluation
* Confusion matrix visualization
* Feature importance analysis
* End-to-end IDS validation
* Clean-environment reproducibility testing

---

## Technology Stack

| Technology         | Purpose                             |
| ------------------ | ----------------------------------- |
| Python 3.13.14     | Core programming language           |
| Scapy 2.7.0        | Packet capture and network analysis |
| Pandas 3.0.5       | Dataset and feature processing      |
| NumPy 2.5.2        | Numerical computation               |
| Scikit-learn 1.9.0 | Machine learning                    |
| Joblib 1.5.3       | Model serialization                 |
| Matplotlib 3.11.1  | Visualization                       |
| Seaborn 0.13.2     | Evaluation visualization            |
| Kali Linux         | Development and testing environment |
| Oracle VirtualBox  | Virtualized test environment        |

---

## System Architecture

```text
                         ┌─────────────────────┐
                         │   Network Traffic   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Scapy Capture     │
                         │      Module         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Feature Extraction  │
                         │      Module         │
                         └──────────┬──────────┘
                                    │
                         ┌──────────▼──────────┐
                         │   ML Classification │
                         │  Random Forest      │
                         └──────────┬──────────┘
                                    │
                         ┌──────────▼──────────┐
                         │ Real-Time Detection │
                         └──────────┬──────────┘
                                    │
                         ┌──────────▼──────────┐
                         │  Alert Management   │
                         └──────────┬──────────┘
                                    │
                         ┌──────────▼──────────┐
                         │ Alert Monitoring &  │
                         │    Statistics       │
                         └─────────────────────┘
```

---

## Machine Learning Model

The project uses a **Random Forest Classifier** for network traffic classification.

The trained model is stored at:

```text
models/random_forest_model.pkl
```

Model validation confirmed:

```text
Model Type : RandomForestClassifier
Features   : 6
Trees      : 100
```

The model operates on six extracted traffic features used during the project's feature engineering and training pipeline.

---

## Detection Pipeline

The real-time detection process performs the following operations:

1. Select a network interface.
2. Capture live packets using Scapy.
3. Extract the required packet features.
4. Convert the extracted features into the model input format.
5. Pass the feature vector to the trained Random Forest classifier.
6. Classify the packet as normal or suspicious.
7. Generate an alert when suspicious traffic is detected.
8. Store the alert in `logs/alerts.log`.
9. Analyze generated alerts using the monitoring module.

Example detection output:

```text
[ML DETECTION] 10.0.3.15 -> 10.0.3.2 | ICMP | len=98 | prediction=normal
```

Example suspicious detection:

```text
[ML DETECTION] N/A -> N/A | OTHER | len=64 | prediction=suspicious

[ALERT] 2026-09-04 18:13:19 |
Prediction=suspicious |
N/A:0 -> N/A:0 |
Protocol=OTHER |
Length=64
```

---

## Alert Monitoring

Generated alerts are stored in:

```text
logs/alerts.log
```

The monitoring module provides:

* Total alert count
* Protocol distribution
* Source IP distribution
* Destination IP distribution
* Average packet length
* Minimum packet length
* Maximum packet length

Example monitoring output:

```text
Total alerts       : 5

Protocol Distribution:
  OTHER     : 5

Source IP Distribution:
  N/A       : 5

Destination IP Distribution:
  N/A       : 5

Packet Length Statistics:
  Average : 64.00 bytes
  Minimum : 64 bytes
  Maximum : 64 bytes
```

---

## Model Evaluation

The project includes an evaluation module for assessing the trained model.

Evaluation artifacts are stored under:

```text
results/evaluation/
```

Current evaluation outputs include:

```text
confusion_matrix.png
feature_importance.csv
feature_importance.png
metrics.txt
```

These artifacts provide visual and numerical insight into model performance and feature contribution.

---

## Project Structure

```text
Ai-Network-Intrusion-Detection-System/
│
├── data/
│   ├── raw/
│   │   ├── labeled_packets.csv
│   │   ├── normal_capture_backup.csv
│   │   ├── normal_traffic.csv
│   │   ├── suspicious_nmap_scan.csv
│   │   └── suspicious_traffic.csv
│   │
│   └── processed/
│       ├── features.csv
│       └── labeled_traffic.csv
│
├── docs/
│   └── reports/
│       ├── phase-0-project-setup-report.md
│       ├── phase-1-environment-setup-report.md
│       ├── phase-2-packet-capture-and-feature-extraction-report.md
│       ├── phase-3-dataset-preparation-and-feature-engineering-report.md
│       ├── phase-4-machine-learning-model-training-report.md
│       ├── phase-5-real-time-ml-detection-and-alerting-report.md
│       ├── phase-6-alert-monitoring-and-detection-statistics-report.md
│       ├── phase-7-end-to-end-ids-integration-report.md
│       ├── phase-8-ids-performance-evaluation-and-visualization-report.md
│       ├── phase-9-end-to-end-detection-validation-report.md
│       └── phase-10-deployment-and-reproducibility-validation-report.md
│
├── logs/
│   ├── alerts.log
│   ├── alerts-phase8-backup.log
│   └── captured_packets.csv
│
├── models/
│   └── random_forest_model.pkl
│
├── results/
│   └── evaluation/
│       ├── confusion_matrix.png
│       ├── feature_importance.csv
│       ├── feature_importance.png
│       └── metrics.txt
│
├── src/
│   ├── alerts/
│   │   └── alert_manager.py
│   │
│   ├── capture/
│   │   └── sniffer.py
│   │
│   ├── detection/
│   │   └── realtime_detector.py
│   │
│   ├── evaluation/
│   │   ├── __init__.py
│   │   └── evaluate_model.py
│   │
│   ├── features/
│   │   └── extractor.py
│   │
│   ├── integration/
│   │   ├── __init__.py
│   │   └── ids_runner.py
│   │
│   ├── model/
│   │   └── train.py
│   │
│   └── monitoring/
│       ├── __init__.py
│       └── alert_monitor.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yuvarajcybersec/Ai-Network-Intrusion-Detection-System.git
cd Ai-Network-Intrusion-Detection-System
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate the Environment

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Verify the Installation

Check the installed Python version:

```bash
python --version
```

Test the required packages:

```bash
python -c "
import scapy
import pandas
import sklearn
import joblib
import matplotlib
import numpy

print('All required packages imported successfully.')
"
```

Load the trained model:

```bash
python -c "
import joblib

model = joblib.load('models/random_forest_model.pkl')

print('Model loaded successfully.')
print('Model type:', type(model).__name__)
print('Features:', model.n_features_in_)
print('Trees:', model.n_estimators)
"
```

---

## Running the IDS

> **Note:** Live packet capture generally requires root privileges on Linux.

First identify available interfaces:

```bash
ip -br addr
```

For the tested Kali Linux environment, `eth1` was the active NAT interface used for the IDS validation.

Run the integrated IDS:

```bash
sudo ./venv/bin/python -c "
from src.integration.ids_runner import run_ids
run_ids(interface='eth1', packet_limit=10)
"
```

The interface should be changed to match the network interface available in the user's own lab environment.

---

## Alert Monitoring

After running the IDS, inspect the alert log:

```bash
cat logs/alerts.log
```

Count alerts:

```bash
wc -l logs/alerts.log
```

Run the monitoring module:

```bash
./venv/bin/python -m src.monitoring.alert_monitor
```

---

## Packet Capture

The packet capture module can be tested directly with an appropriate interface:

```bash
sudo ./venv/bin/python src/capture/sniffer.py
```

The capture module uses Scapy to inspect live traffic and extract packet-level information.

---

## Model Evaluation

The evaluation module can be executed using:

```bash
./venv/bin/python src/evaluation/evaluate_model.py
```

Evaluation results are stored in:

```text
results/evaluation/
```

---

## Validation & Testing

The project was developed and validated progressively through twelve structured phases, covering environment preparation, network traffic acquisition, feature engineering, machine learning, real-time intrusion detection, alert management, system integration, performance evaluation, automated testing, deployment reproducibility, and final repository validation.

| Phase    | Description                               | Status     |
| -------- | ----------------------------------------- | ---------- |
| Phase 0  | Project Setup                             | ✅ Complete |
| Phase 1  | Environment Setup                         | ✅ Complete |
| Phase 2  | Packet Capture & Feature Extraction       | ✅ Complete |
| Phase 3  | Dataset Preparation & Feature Engineering | ✅ Complete |
| Phase 4  | Machine Learning Model Training           | ✅ Complete |
| Phase 5  | Real-Time ML Detection & Alerting         | ✅ Complete |
| Phase 6  | Alert Monitoring & Detection Statistics   | ✅ Complete |
| Phase 7  | End-to-End IDS Integration                | ✅ Complete |
| Phase 8  | Performance Evaluation & Visualization    | ✅ Complete |
| Phase 9  | End-to-End Detection Validation           | ✅ Complete |
| Phase 10 | Deployment & Reproducibility Validation      | ✅ Complete |
| Phase 11 | Automated Testing & Feature Validation       | ✅ Complete |
| Phase 12 | Final Repository Validation & Project Review | ✅ Complete |

---

## Phase 12 Final Repository Validation & Project Review

Phase 12 represents the final validation and release-readiness stage of the AI-Based Network Intrusion Detection System.

This phase consolidates the final repository integrity review, automated testing, source compilation, machine-learning model validation, dataset validation, evaluation artifact verification, alert monitoring validation, documentation review, and Git repository verification.

The final validation confirmed:

```text
Automated test suite             : 26 passed
Python source compilation        : PASS
Random Forest model validation   : PASS
Feature dataset validation       : PASS
Evaluation artifacts             : PASS
Alert monitoring validation      : PASS
Repository integrity             : PASS
Git diff validation              : PASS
Documentation review             : PASS
Git working tree                 : CLEAN
```

Detailed documentation:

```text
docs/reports/phase-12-final-project-validation-and-review-report.md
```

**Final Project Status: COMPLETED**

---

## Phase 10 Deployment Validation

The final validation phase tested the project in an independent Python environment.

The following checks were completed successfully:

```text
Requirements installation       : PASS
Package imports                 : PASS
Random Forest model loading     : PASS
Python source compilation      : PASS
Repository integrity            : PASS
```

A clean virtual environment was created at:

```text
/tmp/ids-deployment-test
```

Dependencies were installed using only:

```text
requirements.txt
```

The trained model loaded successfully with:

```text
RandomForestClassifier
6 features
100 trees
```

This provides evidence that the core project environment can be reproduced outside the original development virtual environment.

---

## Security & Ethical Use

This project is intended for **authorized cybersecurity research, education, and controlled laboratory environments**.

Only capture and analyze network traffic that you are authorized to monitor.

For testing, use:

* Your own virtual machines
* Isolated cybersecurity laboratories
* Authorized training environments
* Systems for which you have explicit permission

Do not use the project to monitor or analyze unauthorized networks or systems.

---

## Limitations

The current implementation is a research and educational prototype.

Current limitations include:

* Packet-level classification is based on a limited feature set.
* Detection quality depends on the training data.
* The model may produce false positives or false negatives.
* The current implementation has not been evaluated under sustained production-scale traffic.
* No production-grade dashboard is currently included.
* No Docker or systemd deployment configuration is included.
* The system has primarily been validated in a Kali Linux virtualized laboratory environment.

These limitations provide opportunities for future improvements.

---

## Future Improvements

Potential future enhancements include:

* Expand the training dataset with additional attack categories.
* Add more network traffic features.
* Improve feature engineering.
* Compare Random Forest with other ML algorithms.
* Add threshold-based confidence scoring.
* Develop a web-based monitoring dashboard.
* Add automated alert severity classification.
* Add database-backed alert storage.
* Add automated testing.
* Add Docker deployment.
* Add CI/CD validation.
* Perform long-duration and high-volume traffic testing.
* Evaluate the system against additional benchmark datasets.

---

## Learning Outcomes

This project provided practical experience in:

* Linux networking
* Kali Linux
* Python programming
* Scapy packet capture
* Network traffic analysis
* Feature engineering
* Dataset preparation
* Machine learning
* Random Forest classification
* Real-time detection
* Security alert generation
* Model evaluation
* Git and GitHub
* Virtual environments
* Deployment reproducibility

---

## Documentation

Detailed development reports for each phase are available in:

```text
docs/reports/
```

The reports document the implementation, testing, validation, and results of the project from initial setup through deployment reproducibility validation.

---

## Author

**Yuvaraj S**

Cybersecurity & AI Enthusiast

GitHub: `yuvarajcybersec`

---

## License

This project is provided for educational and research purposes. See the `LICENSE` file for the applicable license terms.
