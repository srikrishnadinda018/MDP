import pickle
import streamlit as st
from streamlit_option_menu import option_menu





# loading the saved models
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
cancer_disease_model = pickle.load(open('cancer_diseases_model.sav', 'rb'))
parkinson_disease_model = pickle.load(open('perkinson_disease_model.sav', 'rb'))






# sidebar for navigation

with st.sidebar:

    

    selected = option_menu('MULTIPLE DISEASE PREDICTION SYSTEM',

                          

                          ['HOME',
                          'HEART DISEASE PREDICTION',
                          'CANCER DISEASE PREDICTION',
                          'PARKINSON DISEASE PREDICTION',
                          'CONCLUSION'],

                          

                          default_index=0)

    

    


 




# (1) Heart Disease Prediction Page

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










# (2) Cancer Disease Prediction Page

if (selected == 'Cancer Disease Prediction'):

    # page title

    st.title('Cancer Disease Prediction using ML')
    radius_mea = st.text_input('radius_mea')
    texture_mea = st.text_input('texture_mea')
    perimeter_mea = st.text_input('perimeter_mea')
    area_mea = st.text_input('area_mea')
    smoothness_mea = st.text_input('smoothness_mea')

    # code for Prediction
    Cancer_diagnosis = ''

    # creating a button for Prediction

    if st.button('Cancer Disease Test Result'):

        cancer_prediction = cancer_disease_model.predict([[radius_mea,texture_mea,perimeter_mea,area_mea,smoothness_mea]])

        if (cancer_prediction[0] == 1):
          Cancer_diagnosis = 'The person may not have any cancer disease(B)'

        else:
          Cancer_diagnosis = 'The person may have any cancer disease(M)'

        

    st.success(Cancer_diagnosis)
      








# (3) Parkinson Disease Prediction Page

if (selected == 'PARKINSON DISEASE PREDICTION'):

    # page title

    st.title('Parkinson Disease Prediction using ML')
    MDVPFo = st.text_input('MDVP:Fo(Hz)')
    MDVPFhi = st.text_input('MDVP:Fhi(Hz)')
    MDVPFlo = st.text_input('MDVP:Flo(Hz)')
    MDVPJitter = st.text_input('MDVP:Jitter(%)')
    MDVPJitter = st.text_input('MDVP:Jitter(Abs)')
    MDVPRAP = st.text_input('MDVP:RAP')
    MDVPPPQ = st.text_input('MDVP:PPQ')
    JitterDD = st.text_input('Jitter:DD')
    MDVPShimmer = st.text_input('MDVP:Shimmer')
    MDVPShimmer = st.text_input('MDVP:Shimmer(dB)')
    ShimmerAPQ3 = st.text_input('Shimmer:APQ3')
    ShimmerAPQ5 = st.text_input('Shimmer:APQ5')
    MDVPAPQ = st.text_input('MDVP:APQ')
    ShimmerDDA = st.text_input('Shimmer:DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')
    
    # code for Prediction
    parkinson_diagnosis = ''

    # creating a button for Prediction

    if st.button('Parkinson Disease Test Result'):

        parkinson_prediction = perkinson_disease_model.predict([[MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitter,MDVPRAP,MDVPPPQ,JitterDD,MDVPShimmer,MDVPShimmer,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          

        

        if (parkinson_prediction[0] == 1):
          parkinson_diagnosis = 'The person is having parkinson disease'

        else:
          parkinson_diagnosis = 'The person does not have any parkinson disease'

        

    st.success(parkinson_diagnosis)
