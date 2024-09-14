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

def predict_dessert(prot_per_100cal):
    if model:
        input_data = pd.DataFrame([[prot_per_100cal]], columns=["prot_per_100cal"])
        prediction = model.predict(input_data)
        return int(prediction[0])
    else:
        st.error("Model is not loaded. Prediction cannot be made.")
        return None

def run():
    st.title("Dessert Prediction Based on Protein per 100 Calories")

    # Input from user
    prot_per_100cal = st.number_input("Enter protein per 100 calories:", min_value=0.0, step=0.1)

    # When the user clicks the "Predict" button
    if st.button("Predict"):
        # Perform prediction
        result = predict_dessert(prot_per_100cal)

        if result is not None:
            # Display result
            if result == 1:
                st.success("The item is likely a dessert!")
            else:
                st.success("The item is not a dessert.")
        else:
            st.error("Prediction could not be made.")

if __name__ == '__main__':
    run()
