import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu





# loading the saved models

cancer_disease_model = pickle.load(open('cancer_disease_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
#parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))






# sidebar for navigation

with st.sidebar:

    

    selected = option_menu('Multiple Disease Prediction System',

                          

                          ['Home',
                          'Heart Disease Prediction',
                          'Cancer Disease Prediction',
                          'Conclusion'],

                          

                          default_index=0)

    

    


 




# Heart Disease Prediction Page

if (selected == 'Heart Disease Prediction'):

    # page title

    st.title('Heart Disease Prediction using ML')
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          

        

        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'

        else:
          heart_diagnosis = 'The person does not have any heart disease'

        

    st.success(heart_diagnosis)










# Cancer Disease Prediction Page

if (selected == 'Cancer Disease Prediction'):

    # page title

    st.title('Cancer Disease Prediction using ML')
   
    input_values = st.text_input('Enter all the medical information')
    # change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_values)
    # reshape the numpy array as we are predicting for one datapoint
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)








    
    
    # code for Prediction
    Cancer_diagnosis = ''

    # creating a button for Prediction

    if st.button('Cancer Disease Test Result'):

        cancer_prediction = cancer_disease_model.predict(input_data_reshaped)

        if (cancer_prediction[0] == 1):
          Cancer_diagnosis = 'The person is having cancer disease'

        else:
          Cancer_diagnosis = 'The person does not have any cancer disease'

        

    st.success(Cancer_diagnosis)                                                          
