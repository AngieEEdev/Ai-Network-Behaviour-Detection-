import os
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib

from preprocessing import load_data, clean_data, label_data
from features import extract_features
from models import train_model


# path setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "UNSW_NB15_training-set.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")



print("Loading data...")
df = load_data(DATA_PATH)

print("Cleaning data...")
df = clean_data(df)


# split label
print("Splitting features and labels...")
X, y = label_data(df)


#feature
print("Extracting features...")
X = extract_features(X)


# train/split
print("Splitting train/test...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# train
print("Training model...")
model = train_model(X_train, y_train)

print("Model trained successfully")


#save
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

joblib.dump(model, MODEL_PATH)

print(f"Model saved to {MODEL_PATH}")


#quick validation
print("Running quick validation...")

accuracy = model.score(X_test, y_test)
print(f"Validation Accuracy: {accuracy:.2f}")