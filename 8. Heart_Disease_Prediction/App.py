import streamlit as st
import pandas as pd
import joblib as jb

model = jb.load('heart_disease_model.pkl')

st.title("Heart Disease Prediction App")

st.markdown('Please Enter the Following Details')

st.divider()

general_health_map = {'Poor': 0, 'Fair': 1, 'Good': 2, 'Very Good': 3, 'Excellent': 4}
checkup_map = {'Never': 0, '5 or more years ago': 1, 'Within past 5 years': 2,
               'Within the past 2 years': 3, 'Within the past year': 4}
binary_map = {'No': 0, 'Yes': 1}
sex_map = {'Female': 0, 'Male': 1}
age_category_map = {'18-24': 0, '25-29': 1, '30-34': 2, '35-39': 3, '40-44': 4,
                    '45-49': 5, '50-54': 6, '55-59': 7, '60-64': 8,
                    '65-69': 9, '70-74': 10, '75-79': 11, '80+': 12}

General_Health = general_health_map[st.selectbox('General Health', list(general_health_map.keys()))]
Checkup = checkup_map[st.selectbox('Checkup Frequency', list(checkup_map.keys()))]
Exercise = binary_map[st.selectbox('Exercise', list(binary_map.keys()))]

Skin_Cancer = binary_map[st.selectbox('Skin Cancer', list(binary_map.keys()))]
Other_Cancer = binary_map[st.selectbox('Other Cancer', list(binary_map.keys()))]

Depression = binary_map[st.selectbox('Depression', list(binary_map.keys()))]
Diabetes = binary_map[st.selectbox('Diabetes', list(binary_map.keys()))]
Arthritis = binary_map[st.selectbox('Arthritis', list(binary_map.keys()))]

Sex = sex_map[st.selectbox('Sex', list(sex_map.keys()))]
Age_Category = age_category_map[st.selectbox('Age Category', list(age_category_map.keys()))]

Height = st.number_input('Height (in cm)', min_value=0, max_value=300, value=170)
Weight = st.number_input('Weight (in kg)', min_value=0, max_value=300, value=70)
BMI = st.number_input('BMI', min_value=0.0, max_value=100.0, value=22.5)

Smoking_History = binary_map[st.selectbox('Smoking History', list(binary_map.keys()))]
Alcohol_Consumption = st.number_input('Alcohol Consumption (per week)', min_value=0, max_value=30, value=0)

Fruit_Consumption = int(st.selectbox('Fruit Consumption', [
    '30', '12', '8', '16', '2', '1', '60', '0', '7', '5', '3',
    '6', '90', '28', '20', '4', '80', '24', '15', '10', '25', '14',
    '120', '32', '40', '17', '45', '100', '9', '99', '96', '35', '50',
    '56', '48', '27', '72', '36', '84', '26', '23', '18', '21', '42',
    '22', '11', '112', '29', '64', '70', '33', '76', '44', '39', '75',
    '31', '92', '104', '88', '65', '55', '13', '38', '63', '97', '108',
    '19', '52', '98', '37', '68', '34', '41', '116', '54', '62', '85'
]))

Green_Vegetables_Consumption = int(st.selectbox('Green Vegetables Consumption', [
 '16', '0', '3', '30', '4', '12', '8', '20', '1', '10', '5',
 '2', '6', '60', '28', '25', '14', '40', '7', '22', '24', '15',
 '120', '90', '19', '13', '11', '80', '27', '17', '56', '18', '9',
 '21', '99', '29', '31', '45', '23', '100', '104', '32', '48', '75',
 '36', '35', '112', '26', '50', '33', '96', '52', '76', '84', '34',
 '97', '88', '98', '68', '92', '55', '95', '64', '124', '61', '65',
 '77', '85', '44', '39', '70', '93', '128', '37', '53'
]))

FriedPotato_Consumption = int(st.selectbox('Fried Potato Consumption', [
 '12', '4', '16', '8', '0', '1', '2', '30', '20', '15', '10',
 '3', '7', '28', '5', '9', '6', '120', '32', '14', '60', '33',
 '48', '25', '24', '21', '90', '13', '99', '17', '18', '40',
 '56', '34', '36', '44', '100', '11', '64', '45', '80', '29',
 '68', '26', '50', '22', '95', '23', '27', '112', '35', '31',
 '98', '96', '88', '92', '19', '76', '49', '97', '128', '41',
 '37', '42', '52', '72', '46', '124', '84'
]))

if st.button('Predict'):
    user_input = pd.DataFrame({
        'General_Health': [General_Health],
        'Checkup': [Checkup],
        'Exercise': [Exercise],
        'Skin_Cancer': [Skin_Cancer],
        'Other_Cancer': [Other_Cancer],
        'Depression': [Depression],
        'Diabetes': [Diabetes],
        'Arthritis': [Arthritis],
        'Sex': [Sex],                         
        'Age_Category': [Age_Category],
        'Height': [Height],
        'Weight': [Weight],
        'BMI': [BMI],
        'Smoking_History': [Smoking_History],
        'Alcohol_Consumption': [Alcohol_Consumption],
        'Fruit_Consumption': [Fruit_Consumption],
        'Green_Vegetables_Consumption': [Green_Vegetables_Consumption],
        'FriedPotato_Consumption': [FriedPotato_Consumption]
    })

    prediction = model.predict(user_input)[0]

    st.subheader(f"Prediction Result: '{int(prediction)}'")
    if prediction == 1:
        st.error('You are at risk of heart disease.')
    else:
        st.success('You are not at risk of heart disease.')
    

