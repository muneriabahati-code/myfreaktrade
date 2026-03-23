import joblib
import numpy as np # Good to have for formatting data for ML

# Load your AI Model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    st.error("🚨 model.pkl not found! Make sure it is in the same folder as this script.")
    st.stop()
