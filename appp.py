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

    st.subheader("Predict for Dataset")

    # Sample DataFrame (Replace with your actual dataset loading code)
    # Assuming df is already loaded in your environment
    df = pd.DataFrame({
        'title': ['Lentil, Apple, and Turkey Wrap', 'Boudin Blanc Terrine with Red Onion Confit', 'Potato and Fennel Soup Hodge', 'Mahi-Mahi in Tomato Olive Sauce', 'Spinach Noodle Casserole', 'The Best Blts', 'Ham and Spring Vegetable Salad with Shallot Vinaigrette', 'Spicy-Sweet Kumquats', 'Korean Marinated Beef', 'Ham Persillade with Mustard Potato Salad and Mashed Peas', 'Yams Braised with Cream, Rosemary and Nutmeg', 'Spicy Noodle Soup', 'Banana-Chocolate Chip Cake With Peanut Butter Frosting', 'Beef Tenderloin with Garlic and Brandy'],
        'calories': [426, 403, 165, 7040.545899, 547, 948, 7040.545899, 7040.545899, 170, 602, 256, 7040.545899, 766, 174],
        'protein': [30, 18, 6, 125.8419839, 20, 19, 125.8419839, 125.8419839, 7, 23, 4, 125.8419839, 12, 11],
        'fat': [7, 23, 7, 369.0095252, 32, 79, 369.0095252, 369.0095252, 10, 41, 5, 369.0095252, 48, 12],
        'sodium': [559, 1439, 165, 7195.360771, 452, 1042, 7195.360771, 7195.360771, 1272, 1696, 30, 7195.360771, 439, 176],
        'category': ['Wrap', 'Terrine', 'Soup', 'Sauce', 'Casserole', 'Blts', 'Salad', 'Kumquats', 'Beef', 'Salad', 'Yams', 'Soup', 'Cake', 'Tenderloin']
    })

    # Predict category for each recipe
    if st.button("Predict Dataset"):
        def predict_category_for_row(calories, protein, fat, sodium):
            return predict_category(calories, protein, fat, sodium)

        df['prediction'] = df.apply(lambda row: predict_category_for_row(row['calories'], row['protein'], row['fat'], row['sodium']), axis=1)

        st.write(df[['title', 'category', 'prediction']])

if __name__ == '__main__':
    run()
