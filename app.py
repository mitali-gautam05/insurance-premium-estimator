import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Insurance Premium Prediction",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Insurance Premium Prediction")
st.write("Fill in the details below to predict the insurance premium category.")

st.divider()

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=25
)

weight = st.number_input(
    "Weight (kg)",
    min_value=20.0,
    max_value=200.0,
    value=70.0
)

height = st.number_input(
    "Height (m)",
    min_value=1.00,
    max_value=2.50,
    value=1.70,
    step=0.01
)

income_lpa = st.number_input(
    "Income (LPA)",
    min_value=0.0,
    value=5.0
)

smoker = st.checkbox("Smoker")

city = st.text_input(
    "City",
    placeholder="Delhi"
)

occupation = st.selectbox(
    "Occupation",
    [
        "private_job",
        "government_job",
        "business_owner",
        "freelancer",
        "student",
        "retired",
        "unemployed"
    ]
)

st.divider()

if st.button("Predict"):

    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:

            result = response.json()["response"]

            st.success("Prediction Successful")

            st.subheader("Prediction")

            st.write(f"**Predicted Category:** {result['predicted_category']}")

            st.write(f"**Confidence:** {result['confidence']*100:.2f}%")

            st.subheader("Class Probabilities")

            st.json(result["class_probabilities"])

        else:

            st.error("Prediction Failed")
            st.json(response.json())

    except requests.exceptions.ConnectionError:

        st.error("FastAPI server is not running.")