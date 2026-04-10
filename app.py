import streamlit as st
import pandas as pd
import joblib
import os

from src.features import extract_features


#config page
st.set_page_config(page_title="AI Network Behaviour Detection", layout="wide")

st.title("AI Network Behaviour Detection Dashboard")


# load model
MODEL_PATH = "models/model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model not found. Please run training first.")
    st.stop()

try:
    model = joblib.load(MODEL_PATH)
    st.success("Model loaded successfully")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()


# upload file
st.header("Upload Network Data (CSV)")

file = st.file_uploader("Upload CSV file", type=["csv"])

if file:
    try:
        # data loading
        df = pd.read_csv(file)
        df.columns = df.columns.str.strip()

        st.subheader("Data Preview")
        st.dataframe(df)

        
        features = extract_features(df)

        
        prediction = model.predict(features)

        # predictions
        st.subheader("Model Predictions")
        st.write(prediction)

        # result display
        if prediction.mean() > 0.5:
            st.error("Anomalous Behaviour Detected")
        else:
            st.success("Normal Behaviour")

    except Exception as e:
        st.error(f"Error processing file: {e}")