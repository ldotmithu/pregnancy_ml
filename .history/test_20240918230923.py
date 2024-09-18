import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Load the trained model and preprocessor
model = joblib.load(Path('artifacts/model_train/model.joblib'))
churn_preprocess = joblib.load(Path('artifacts/model_train/preprocess.joblib'))

# Set up the Streamlit page configuration
st.set_page_config(page_title="Mental Risk Prediction", layout="wide")

# Add a custom CSS to style the app
st.markdown("""
    <style>
    .main { 
        background-color: #f0f2f6; 
        padding: 20px;
    }
    .sidebar .sidebar-content { 
        background-color: #ffffff; 
    }
    h1 {
        color: #0d6efd;
        font-size: 2rem;
    }
    .stButton button {
        background-color: #0d6efd;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .stSelectbox {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

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
    try:
        input_data_preprocessed = churn_preprocess.transform(input_data)
    except ValueError as e:
        st.error(f"Error in preprocessing: {e}")
        input_data_preprocessed = None

    # Predict mental risk
    if st.button("Predict") and input_data_preprocessed is not None:
        prediction = model.predict(input_data_preprocessed)[0]
        st.success(f"Prediction: {prediction}")

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

