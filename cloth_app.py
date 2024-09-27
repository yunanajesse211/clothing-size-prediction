import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder


#Load model
model = pickle.load(open('model.pkl', 'rb'))

def predict_size(input_data):
    size_labels = ['L', 'M', 'S', 'XL', 'XXL', 'XXS', 'XXXL']
    label_encoder = LabelEncoder()
    label_encoder.fit(size_labels)
    prediction = model.predict(input_data)
    predicted_size = label_encoder.inverse_transform(prediction)
    return predicted_size

#Main App
st.title("Clothing Size Prediction")
weight = st.number_input('Weight (in kg)', min_value=20.0, max_value=500.0, step=1.0)
age = st.number_input('Age', min_value=10, max_value=120, step=1)
height = st.number_input('Height (in cm)', min_value=100.0, max_value=500.0, step=1.0)

if st.button('Predict Clothing Size'):
    if weight > 0 and age > 0 and height > 0:
        bmi=height/weight
        input_data = [[age, height,weight,bmi]]
        predicted_size = predict_size(input_data)
        st.success(f"The predicted clothing size is: {predicted_size[0]}")
    else:
        st.warning("Please fill in all the required fields.")