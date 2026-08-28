import pandas as pd
from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


INPUT_FILE = "data/processed/features.csv"
MODEL_FILE = "models/random_forest_model.pkl"


def train_model():

    print("=" * 60)
    print("AI-Based Network Intrusion Detection System")
    print("Phase 4: Machine Learning Model Training")
    print("=" * 60)

    # Load engineered feature dataset
    df = pd.read_csv(INPUT_FILE)

    print(f"Input dataset : {INPUT_FILE}")
    print(f"Dataset shape : {df.shape}")

    # Separate features and target
    X = df.drop(columns=["label_encoded"])
    y = df["label_encoded"]

    print(f"Features      : {X.shape[1]}")
    print(f"Samples       : {X.shape[0]}")

    print("\nClass distribution:")
    print(y.value_counts())

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42,
        stratify=y
    )

    print("\nDataset split:")
    print(f"Training samples : {len(X_train)}")
    print(f"Testing samples  : {len(X_test)}")

    # Create Random Forest classifier
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced"
    )

    # Train model
    print("\nTraining Random Forest model...")
    model.fit(X_train, y_train)

    print("Training completed successfully.")

    # Generate predictions
    y_pred = model.predict(X_test)

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

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
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

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

    # Save trained model
    Path(MODEL_FILE).parent.mkdir(parents=True, exist_ok=True)

    import joblib
    joblib.dump(model, MODEL_FILE)

    print("\nModel saved successfully:")
    print(MODEL_FILE)

    print("=" * 60)


if __name__ == "__main__":
    train_model()
