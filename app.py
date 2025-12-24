import streamlit as st
import numpy as np
import pickle

# ---------------------------------
# Load model
# ---------------------------------
with open("finalized_RFmodel.sav", "rb") as f:
    model = pickle.load(f)

# ---------------------------------
# Manual mappings for categorical columns
# ---------------------------------
gender_map = {'male': 0, 'female': 1}
school_type_map = {'public': 0, 'private': 1}
parent_education_map = {'high_school': 0, 'bachelor': 1, 'master': 2}
internet_access_map = {'no': 0, 'yes': 1}
extra_activities_map = {'no': 0, 'yes': 1}
study_method_map = {'group': 0, 'solo': 1}

# ---------------------------------
# Page Title
# ---------------------------------
st.title("Sindhu's Student Final Grade Prediction 📚")
st.write("Enter student details to predict the final grade.")

st.subheader("Student Details")

# ---------------------------------
# Inputs
# ---------------------------------
student_id = st.number_input("Student ID (unique integer)", 1, 10000, 1)
age = st.number_input("Age", 5, 25, 16)
gender = st.selectbox("Gender", ["male", "female"])
school_type = st.selectbox("School Type", ["public", "private"])
parent_education = st.selectbox("Parent Education", ["high_school", "bachelor", "master"])
study_hours = st.number_input("Study Hours per Day", 0, 24, 2)
attendance_percentage = st.number_input("Attendance Percentage", 0, 100, 90)
internet_access = st.selectbox("Internet Access", ["yes", "no"])
travel_time = st.number_input("Travel Time to School (in minutes)", 0, 180, 30)
extra_activities = st.selectbox("Extra Activities", ["yes", "no"])
study_method = st.selectbox("Study Method", ["group", "solo"])
math_score = st.number_input("Math Score", 0, 100, 75)
science_score = st.number_input("Science Score", 0, 100, 70)
english_score = st.number_input("English Score", 0, 100, 80)
overall_score = st.number_input("Overall Score (average)", 0, 100, 75)

# ---------------------------------
# Prepare input
# ---------------------------------
user_values = [
    student_id,
    age,
    gender_map[gender],
    school_type_map[school_type],
    parent_education_map[parent_education],
    study_hours,
    attendance_percentage,
    internet_access_map[internet_access],
    travel_time,
    extra_activities_map[extra_activities],
    study_method_map[study_method],
    math_score,
    science_score,
    english_score,
    overall_score
]

input_data = np.array(user_values).reshape(1, -1)

# ---------------------------------
# Prediction
# ---------------------------------
if st.button("Predict Final Grade"):
    prediction = model.predict(input_data)[0]

    # Grade interpretation
    if prediction == 'a':
        interpretation = "Excellent 🤩"
    elif prediction == 'b' or prediction=='c':
        interpretation = "Good 😊"
    elif prediction == 'd':
        interpretation = "Average 🙂"
    else:  
        interpretation = "Poor 😖"

    st.success(f"Predicted Final Grade: {prediction}")
    st.info(f"Interpretation: {interpretation}")
