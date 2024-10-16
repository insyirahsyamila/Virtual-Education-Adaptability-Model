import numpy as np
import pandas as pd
import streamlit as st
from sklearn import preprocessing
import pickle

model = pickle.load(open('model.pkl', 'rb'))


encoder_dict = pickle.load(open('encoder.pkl', 'rb'))
cols = ['Gender', 'Age_Range', 'Education_Level', 'Institution_Type', 'IT_Student', 
        'Location', 'Load_shedding', 'Financial_Condition', 'Internet_Type',
        'Network_Type', 'Class_Duration', 'Self_Lms', 'Device']

def main():

    st.set_page_config(
        page_title="Virtual Education Adaptivity Predictor",
        page_icon="📘",
        initial_sidebar_state="auto",
    )

    image = "C:/Users/syi/Documents/UNISEL DOC 01/UNISEL DOC/SIDEC TRAINING/CAPSTONE PROJECT/WebApp/study.jpg"
    st.image(image, width=690)

    st.title("Virtual Education Adaptivity Predictor")


    # Collect user input
    Gender = st.selectbox("Gender",['Male', 'Female'])
    Age_Range	= st.selectbox("Age",['21-25', '16-20', '11-15', '26-30', '6-10', '1-5'])
    Education_Level	= st.selectbox("Education Level", ['University', 'College', 'School'])
    Institution_Type = st.selectbox("Institution Type", ['Non Government', 'Government'])	
    IT_Student = st.selectbox("Are you an IT Student?",['No', 'Yes'])
    Location = st.selectbox("Do you live in town area?",['Yes', 'No'])	
    Load_shedding = st.selectbox("Temporary reduction of electric power in your area",['Low', 'High'])	
    Financial_Condition	= st.selectbox("Financial Condition", ['Middle Class', 'Lower Class', 'Upper Class'])
    Internet_Type = st.selectbox("Internet Type", ['Wifi', 'Mobile Data'])
    Network_Type = st.selectbox("Network Type",  ['4G', '3G', '2G'])	
    Class_Duration	= st.selectbox("Class Duration (Hours)", ['3-6', '1-3', '0'])
    Self_Lms = st.selectbox("Do you have a self learning management?", ['No', 'Yes'])	
    Device = st.selectbox("Device", ["Tab", "Mobile", "Computer"])


    if st.button("Predict"):
        
        input_data = {'Gender': Gender, 'Age_Range': Age_Range, 'Education_Level': Education_Level, 'Institution_Type': Institution_Type, 'IT_Student': IT_Student, 
                      'Location': Location, 'Load_shedding': Load_shedding, 'Financial_Condition': Financial_Condition, 'Internet_Type': Internet_Type,
                      'Network_Type': Network_Type, 'Class_Duration': Class_Duration, 'Self_Lms': Self_Lms, 'Device': Device}
        print(input_data)
        df=pd.DataFrame([list(input_data.values())], columns=['Gender', 'Age_Range', 'Education_Level', 'Institution_Type', 'IT_Student', 
                      'Location', 'Load_shedding', 'Financial_Condition', 'Internet_Type',
                      'Network_Type', 'Class_Duration', 'Self_Lms', 'Device'])
        
        category_col = ['Gender', 'Age_Range', 'Education_Level', 'Institution_Type', 'IT_Student', 
                      'Location', 'Load_shedding', 'Financial_Condition', 'Internet_Type',
                      'Network_Type', 'Class_Duration', 'Self_Lms', 'Device', 'Adaptivity_Level']
        
        for col in df.columns:
            le = encoder_dict[col]
            print(col)
            df[col] = le.transform(df[col])

        features_list = df.values.tolist()
        prediction = model.predict(features_list)

        output = int(prediction[0])
        if output == 0:
            text = "Moderate"
        elif output == 1:
            text = "Low"
        else:
            text = "High"

        st.success('Student Adaptability is {}'.format(text))

if __name__ == '__main__':
    main()
