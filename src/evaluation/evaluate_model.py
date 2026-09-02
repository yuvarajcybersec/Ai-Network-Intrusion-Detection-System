import joblib
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)
from sklearn.model_selection import train_test_split


INPUT_FILE = "data/processed/features.csv"
MODEL_FILE = "models/random_forest_model.pkl"
RESULTS_DIR = Path("results/evaluation")

def generate_visualizations(cm, feature_importance):
    """Generate evaluation visualizations."""

    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # Confusion matrix visualization
    plt.figure(figsize=(6, 5))

    plt.imshow(cm)

    plt.title("IDS Confusion Matrix")
    plt.xlabel("Predicted Label")
    plt.ylabel("Actual Label")

    plt.xticks(
        [0, 1],
        ["Normal", "Suspicious"]
    )

    plt.yticks(
        [0, 1],
        ["Normal", "Suspicious"]
    )

    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(
                j,
                i,
                cm[i, j],
                ha="center",
                va="center"
            )

    plt.tight_layout()

    confusion_matrix_file = (
        RESULTS_DIR / "confusion_matrix.png"
    )

    plt.savefig(
        confusion_matrix_file,
        dpi=150
    )

    plt.close()

    # Feature importance visualization
    plt.figure(figsize=(8, 5))

    sorted_features = feature_importance.sort_values(
        by="importance"
    )

    plt.barh(
        sorted_features["feature"],
        sorted_features["importance"]
    )

    plt.title("Random Forest Feature Importance")
    plt.xlabel("Importance")
    plt.ylabel("Feature")

    plt.tight_layout()

    feature_importance_file = (
        RESULTS_DIR / "feature_importance.png"
    )

    plt.savefig(
        feature_importance_file,
        dpi=150
    )

    plt.close()

    print("\nVisualizations saved:")
    print(f"Confusion matrix : {confusion_matrix_file}")
    print(f"Feature importance: {feature_importance_file}")

def evaluate_model():
    """Evaluate the trained IDS machine-learning model."""

    print("=" * 60)
    print("AI-Based Network Intrusion Detection System")
    print("Phase 8: Model Performance Evaluation")
    print("=" * 60)

    # Load dataset
    df = pd.read_csv(INPUT_FILE)

    print(f"Input dataset : {INPUT_FILE}")
    print(f"Dataset shape : {df.shape}")

    # Separate features and target
    X = df.drop(columns=["label_encoded"])
    y = df["label_encoded"]

    print(f"Features      : {X.shape[1]}")
    print(f"Samples       : {X.shape[0]}")

    # Reproduce the Phase 4 train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42,
        stratify=y
    )

    print("\nEvaluation split:")
    print(f"Training samples : {len(X_train)}")
    print(f"Testing samples  : {len(X_test)}")

    # Load trained model
    print("\nLoading trained model...")

    model = joblib.load(MODEL_FILE)

    print("Model loaded successfully.")
    print(f"Model type   : {type(model).__name__}")
    print(f"Model trees  : {model.n_estimators}")
    print(f"Model features: {model.n_features_in_}")

    # Generate predictions
    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test,
        y_pred,
        zero_division=0
    )
    recall = recall_score(
        y_test,
        y_pred,
        zero_division=0
    )
    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )

    print("\nModel Evaluation")
    print("-" * 40)
    print(f"Accuracy  : {accuracy:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1-Score  : {f1:.4f}")

    # Classification report
    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=["normal", "suspicious"],
            zero_division=0
        )
    )

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    print("Confusion Matrix:")
    print(cm)

    # Feature importance
    feature_importance = pd.DataFrame({
        "feature": X.columns,
        "importance": model.feature_importances_
    }).sort_values(
        by="importance",
        ascending=False
    )

    print("\nFeature Importance:")
    print(feature_importance.to_string(index=False))

    # Save evaluation results
    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    metrics_file = RESULTS_DIR / "metrics.txt"

    with open(metrics_file, "w") as file:
        file.write("Phase 8 – Model Performance Evaluation\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"Dataset: {INPUT_FILE}\n")
        file.write(f"Samples: {len(df)}\n")
        file.write(f"Test samples: {len(X_test)}\n\n")

        file.write("Metrics\n")
        file.write("-" * 30 + "\n")
        file.write(f"Accuracy: {accuracy:.4f}\n")
        file.write(f"Precision: {precision:.4f}\n")
        file.write(f"Recall: {recall:.4f}\n")
        file.write(f"F1-Score: {f1:.4f}\n\n")

        file.write("Confusion Matrix\n")
        file.write("-" * 30 + "\n")
        file.write(str(cm))
        file.write("\n\n")

        file.write("Feature Importance\n")
        file.write("-" * 30 + "\n")
        file.write(
            feature_importance.to_string(index=False)
        )
        file.write("\n")

        feature_file = RESULTS_DIR / "feature_importance.csv"
    feature_importance.to_csv(
        feature_file,
        index=False
    )

    generate_visualizations(
        cm,
        feature_importance
    )

    print("\nEvaluation results saved:")
    print(f"Metrics           : {metrics_file}")
    print(f"Feature importance: {feature_file}")

    print("=" * 60)

if __name__ == "__main__":
    evaluate_model()
