import pickle
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

model = pickle.load(open('knn-paru-paru.sav', 'rb'))

st.title('Estimasi Pasien Yang Menderita Kanker Paru-Paru')


AGE = st.text_input('Usia Pasien')
SMOKING = st.selectbox('Apakah pasien merokok?', ['1', '2'])

if SMOKING == '1':
    SMOKING = NO
elif SMOKING == '2':
    SMOKING = YES
else:
    SMOKING = 0

YELLOW_FINGERS = st.selectbox('Apakah pasien jari pasien kuning?', ['1', '2'])
    
if YELLOW_FINGERS == '1':
    YELLOW_FINGERS = NO
elif YELLOW_FINGERS == '2':
    YELLOW_FINGERS = YES
else:
    YELLOW_FINGERS = 0

ANXIETY = st.selectbox('Apakah pasien mempunyai kecemasan berlebih?', ['1', '2'])
    
if ANXIETY == '1':
    ANXIETY = NO
elif ANXIETY == '2':
    ANXIETY = YES
else:
    ANXIETY = 0

PEER_PRESSURE = st.selectbox('Apakah pasien mempunyai tekanan?', ['1', '2'])
    
if PEER_PRESSURE == '1':
   PEER_PRESSURE = NO
elif PEER_PRESSURE == '2':
    PEER_PRESSURE = YES
else:
    PEER_PRESSURE = 0

COUGHING = st.selectbox('Apakah pasien batuk-batuk?', ['1', '2'])
    
if COUGHING == '1':
   COUGHING = NO
elif COUGHING == '2':
    COUGHING = YES
else:
    COUGHING = 0

SHORTNESS_OF_BREATH = st.selectbox('Apakah pasien sesak nafas?', ['1', '2'])
    
if SHORTNESS_OF_BREATH== '1':
   SHORTNESS_OF_BREATH = NO
elif SHORTNESS_OF_BREATH == '2':
    SHORTNESS_OF_BREATH = YES
else:
    SHORTNESS_OF_BREATH = 0

SWALLOWING_DIFFICULTY = st.selectbox('Apakah pasien kesulitan menelan?', ['1', '2'])
    
if SWALLOWING_DIFFICULTY== '1':
   SWALLOWING_DIFFICULTY = NO
elif SWALLOWING_DIFFICULTY == '2':
    SWALLOWING_DIFFICULTY = YES
else:
    SWALLOWING_DIFFICULTY = 0

CHEST_PAIN = st.selectbox('Apakah pasien nyeri dada?', ['1', '2'])
    
if CHEST_PAIN== '1':
   CHEST_PAIN = NO
elif CHEST_PAIN == '2':
    CHEST_PAIN = YES
else:
    CHEST_PAIN = 0

CHRONIC_DISEASE = st.selectbox('Apakah pasien mempunyai penyakit kronis?', ['1', '2'])
    
if CHRONIC_DISEASE== '1':
   CHRONIC_DISEASE = NO
elif CHRONIC_DISEASE == '2':
    CHRONIC_DISEASE = YES
else:
    CHRONIC_DISEASE = 0

WHEEZING = st.selectbox('Apakah pasien mengi (Napas Berbunyi)?', ['1', '2'])
    
if WHEEZING== '1':
   WHEEZING = NO
elif WHEEZING == '2':
    WHEEZING = YES
else:
    WHEEZING = 0



kelas = ''

if st.button('Estimasi'):
    estimasi_pasien = model.predict([[AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN, CHRONIC_DISEASE, WHEEZING]])
    
    if(estimasi_pasien[0] == 0):
        kanker = 'Pasien menderita kanker paru-paru'
    else :
        kanker ='Pasien tidak menderita kanker paru-paru'

    st.success(kanker)
