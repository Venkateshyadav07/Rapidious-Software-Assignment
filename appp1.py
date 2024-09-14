import streamlit as st
import pickle
import pandas as pd

# Function to load the model
@st.cache_resource
def load_model():
    try:
        with open('rforest_model.pkl', 'rb') as f:
            model = pickle.load(f)
        st.success("Model loaded successfully!")
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please ensure 'rforest_model.pkl' is in the same directory as this script.")
        return None

# Load the model
model = load_model()

def predict_category(calories, protein, fat, sodium):
    if model:
        input_data = pd.DataFrame([[calories, protein, fat, sodium]], columns=["calories", "protein", "fat", "sodium"])
        prediction = model.predict(input_data)
        return prediction[0]
    else:
        st.error("Model is not loaded. Prediction cannot be made.")
        return None

def run():
    st.title("Dish Category Prediction")

    # Input from user
    calories = st.number_input("Enter calories:", min_value=0)
    protein = st.number_input("Enter protein:", min_value=0.0, step=0.1)
    fat = st.number_input("Enter fat:", min_value=0.0, step=0.1)
    sodium = st.number_input("Enter sodium:", min_value=0.0, step=0.1)

    # When the user clicks the "Predict" button
    if st.button("Predict"):
        # Perform prediction
        result = predict_category(calories, protein, fat, sodium)

        if result:
            # Display result
            st.success(f"The item is classified as: {result}")
        else:
            st.error("Prediction could not be made.")

if __name__ == '__main__':
    run()
