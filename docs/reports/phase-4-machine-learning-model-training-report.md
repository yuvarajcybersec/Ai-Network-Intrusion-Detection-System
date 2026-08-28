# Phase 4 — Machine Learning Model Training Report

## AI-Based Network Intrusion Detection System

---

## 1. Phase Overview

Phase 4 implements the machine-learning component of the AI-Based Network Intrusion Detection System.

The objective of this phase is to train a supervised machine-learning classifier using the engineered network traffic features generated during Phase 3.

The trained model classifies network traffic into two categories:

- `normal`
- `suspicious`

A Random Forest classifier was selected as the initial baseline model because it is suitable for structured/tabular data and provides feature-importance information for model interpretation.

---

## 2. Phase Objectives

The objectives of Phase 4 were:

- Load the engineered feature dataset.
- Separate input features from the target label.
- Split the dataset into training and testing subsets.
- Train a Random Forest classifier.
- Generate predictions on unseen test data.
- Evaluate the classifier using standard classification metrics.
- Generate a confusion matrix.
- Determine feature importance.
- Save the trained model for later use by the detection system.
- Verify that the saved model can be successfully loaded.

---

## 3. Input Dataset

The machine-learning pipeline uses the feature dataset generated during Phase 3:

```text
data/processed/features.csv
