import gradio as gr
import pandas as pd
import joblib
from pathlib import Path

# Load the trained model and preprocessor
model = joblib.load(Path('artifacts/model_train/model.joblib'))
churn_preprocess = joblib.load(Path('artifacts/model_train/preprocess.joblib'))

# Define the prediction function
def predict_risk(Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate):
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
        # Predict mental risk
        prediction = model.predict(input_data_preprocessed)[0]
        prediction
    except Exception as e:
        return f"Error: {e}"

# Define the Gradio interface
iface = gr.Interface(
    fn=predict_risk,
    inputs=[
        gr.inputs.Number(label="Age"),
        gr.inputs.Number(label="SystolicBP")
        gr.inputs.Number(label="DiastolicBP")
        gr.inputs.Number(label="BS")
        gr.inputs.Number(label="BodyTemp")
        gr.inputs.Number(label="HeartRate")
    ],
    outputs=gr.outputs.Textbox(label="Prediction"),
    title="Mental Risk Prediction",
    description="Enter the features to predict the mental risk level."
)

# Launch the interface
iface.launch()
