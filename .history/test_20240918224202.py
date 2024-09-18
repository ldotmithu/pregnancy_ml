import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Load the trained model and preprocessor
model = joblib.load(Path('artifacts/model_train/model.joblib'))
churn_preprocess = joblib.load(Path('artifacts/model_train/preprocess.joblib'))

# Create the Streamlit UI with tabs
st.title("Mental Risk Prediction Using Machine Learning")

# Create tabs for "Prediction" and "Feature Explanation"
tabs = st.tabs(["Prediction", "Feature Explanation"])

with tabs[0]:
    st.header("Predict Mental Risk")

    # Input fields for the features
    Age = st.number_input("Age", min_value=0, max_value=150, value=30)
    SystolicBP = st.selectbox("Systolic BP", options=[i for i in range(80, 201)], index=0)
    DiastolicBP = st.selectbox("Diastolic BP", options=[i for i in range(40, 121)], index=0)
    BS = st.selectbox("Blood Sugar", options=["Normal", "High", "Low"], index=0)
    BodyTemp = st.selectbox("Body Temperature", options=[i for i in range(95, 106)], index=0)
    HeartRate = st.selectbox("Heart Rate", options=[i for i in range(30, 201)], index=0)

    # Create a DataFrame from input data
    input_data = pd.DataFrame({
        'Age': [Age],
        'SystolicBP': [SystolicBP],
        'DiastolicBP': [DiastolicBP],
        'BS': [BS],
        'BodyTemp': [BodyTemp],
        'HeartRate': [HeartRate]
    })

    # Preprocess the input data
    input_data_preprocessed = churn_preprocess.transform(input_data)

    # Predict mental risk
    if st.button("Predict"):
        prediction = model.predict(input_data_preprocessed)[0]
        risk_categories = {0: 'Low Risk', 1: 'Mid Risk', 2: 'High Risk'}
        st.write(f"Prediction: {risk_categories.get(prediction, 'Unknown Risk')}")

with tabs[1]:
    st.header("Feature Explanations")

    st.write("""
    ### Feature Explanations:
    - **Age**: Age of the individual in years.
    - **Systolic BP**: Systolic Blood Pressure measured in mm Hg.
    - **Diastolic BP**: Diastolic Blood Pressure measured in mm Hg.
    - **Blood Sugar**: Blood sugar level; categories might be Normal, High, or Low.
    - **Body Temperature**: Body temperature in degrees Fahrenheit or Celsius.
    - **Heart Rate**: Heart rate measured in beats per minute.
    """)
