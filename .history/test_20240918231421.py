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
    Age = st.number_input("Age", min_value=0, max_value=150)
    SystolicBP = st.slider("Systolic BP", min_value=80, max_value=220, value=98)
    DiastolicBP = st.number_input("Diastolic BP", min_value=40, max_value=211)
    BS = st.number_input("BS")
    BodyTemp = st.slider("Body Temperature (°F)", min_value=95, max_value=106, value=98)
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
    try:
        input_data_preprocessed = churn_preprocess.transform(input_data)
    except ValueError as e:
        st.error(f"Error in preprocessing: {e}")
        input_data_preprocessed = None

    # Predict mental risk
    if st.button("Predict") and input_data_preprocessed is not None:
        prediction = model.predict(input_data_preprocessed)[0]
        st.write(f"Prediction: {prediction}")

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
