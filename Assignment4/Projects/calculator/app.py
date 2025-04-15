import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Streamlit app
st.set_page_config(page_title="BMI Calculator", page_icon="💪")

st.title("💪 BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) based on your weight and height.")

# Input fields
weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (m):", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        st.success(f"Your BMI is: {bmi:.2f}")

        # BMI Category
        if bmi < 18.5:
            st.info("You're underweight.")
        elif 18.5 <= bmi < 25:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 30:
            st.warning("You're overweight.")
        else:
            st.error("You're obese.")
    else:
        st.error("Please enter valid weight and height.")
