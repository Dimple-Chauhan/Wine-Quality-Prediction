import streamlit as st
import pickle


with open("best_wine_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🍷 Advanced Wine Quality Prediction App")
st.write("Predict the quality of wine using its chemical properties!")

st.subheader("Enter Wine Features:")


fixed_acidity = st.slider("Fixed Acidity", 0.0, 20.0, 7.0)
volatile_acidity = st.slider("Volatile Acidity", 0.0, 2.0, 0.5)
citric_acid = st.slider("Citric Acid", 0.0, 2.0, 0.3)
residual_sugar = st.slider("Residual Sugar", 0.0, 20.0, 2.0)
chlorides = st.slider("Chlorides", 0.0, 1.0, 0.08)
free_sulfur_dioxide = st.slider("Free Sulfur Dioxide", 0.0, 100.0, 15.0)
total_sulfur_dioxide = st.slider("Total Sulfur Dioxide", 0.0, 300.0, 46.0)
density = st.slider("Density", 0.990, 1.005, 0.996)
pH = st.slider("pH", 2.0, 5.0, 3.3)
sulphates = st.slider("Sulphates", 0.0, 2.0, 0.6)
alcohol = st.slider("Alcohol", 0.0, 20.0, 10.0)
Id = st.slider("ID", 0.0, 20.0, 10.0)


if st.button("🔮 Predict Quality"):
    input_data = [[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                   chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                   pH, sulphates, alcohol, Id]]
    prediction = model.predict(input_data)
    st.success(f"✅ Predicted Wine Quality: {prediction[0]}")
