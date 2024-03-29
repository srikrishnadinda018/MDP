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

if (selected == 'HEART DISEASE PREDICTION'):
    st.image("heart.jpeg",use_column_width=True)

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
      if any(not x for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
        st.error("Please fill all the details.")
      else:
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person is not having  any heart disease'
        
        st.success(heart_diagnosis)



        

    
    st.image("images (1).jpg", caption="Mapping View Of Heart Disease In India", use_column_width=True)
    st.image("images(2).jpeg", caption="Statistical Chart Of Age-Group vs First Time Heart Disease", use_column_width=True)
    st.image("image (3).jpeg", caption="Statistical Chart Of Gender vs First Time Heart Disease", use_column_width=True)










# (2) Cancer Disease Prediction Page

if (selected == 'CANCER DISEASE PREDICTION'):

    # page title
    st.image("Cancer.jpeg",use_column_width=True)

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
        if any(not x for x in [radius_mea,texture_mea,perimeter_mea,area_mea,smoothness_mea]):
            st.error("Please fill all the details.")

        else:
            cancer_prediction = cancer_disease_model.predict([[radius_mea,texture_mea,perimeter_mea,area_mea,smoothness_mea]])
            if (cancer_prediction[0] == 1):
                Cancer_diagnosis = 'The person may not have any cancer disease(B)'
            else:
                Cancer_diagnosis = 'The person may have any cancer disease(M)'
            st.success(Cancer_diagnosis)
                


        

    
    st.image("image (4).jpeg", caption="Mapping View Of Cancer Disease In India", use_column_width=True)
    st.image("images(5).jpg", caption="Statistical Chart Of Age-Group vs First Time Cancer Disease", use_column_width=True)
    st.image("image (6).jpeg", caption="Statistical Chart Of Gender vs First Time Cancer Disease", use_column_width=True)

      








# (3) Parkinson Disease Prediction Page

if (selected == 'PARKINSON DISEASE PREDICTION'):

    # page title
    st.image("Parkinson.jpeg",use_column_width=True)

    st.title('Parkinson Disease Prediction using ML')
    MDVPFo = st.text_input('MDVP:Fo(Hz)')
    MDVPFhi = st.text_input('MDVP:Fhi(Hz)')
    MDVPFlo = st.text_input('MDVP:Flo(Hz)')
    MDVPJitter = st.text_input('MDVP:Jitter(%)')
    MDVPJitte = st.text_input('MDVP:Jitter(Abs)')
    MDVPRAP = st.text_input('MDVP:RAP')
    MDVPPPQ = st.text_input('MDVP:PPQ')
    JitterDD = st.text_input('Jitter:DD')
    MDVPShimmer = st.text_input('MDVP:Shimmer')
    MDVPShimme = st.text_input('MDVP:Shimmer(dB)')
    
    
    # code for Prediction
    parkinson_diagnosis = ''

    # creating a button for Prediction

    if st.button('Parkinson Disease Test Result'):
        if any(not x for x in [MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitte,MDVPRAP,MDVPPPQ,JitterDD,MDVPShimmer,MDVPShimme]):
            st.error("Please fill all the details.")
        else:
            parkinson_prediction = parkinson_disease_model.predict([[MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitte,MDVPRAP,MDVPPPQ,JitterDD,MDVPShimmer,MDVPShimme]])
            if (parkinson_prediction[0] == 1):
                parkinson_diagnosis = 'The person is not having parkinson disease'
            else:
                parkinson_diagnosis = 'The person have any Parkinson disease'
            st.success(parkinson_diagnosis)
        


                                  

    st.image("images (7).jpeg", caption="Statistical View Of Parkinson's Disease In India", use_column_width=True)
    st.image("images (8).png", caption="Statistical Chart Of Age-Group vs First Time Parkinson's Disease", use_column_width=True)
    st.image("images (9).jpg", caption="Statistical Chart Of Gender vs First Time Parkinson's Disease", use_column_width=True)
