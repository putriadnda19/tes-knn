import pickle 
import streamlit as st 

st.title('Estimasi Pasien Yang Menderita Kanker Paru-Paru')

AGE = st.number_input('Input umur pasien')

SMOKING = ['YES', 'NO']
SMOKING = st.radio('Apakah pasien merokok?', SMOKING)

YELLOW_FINGERS = ['YES', 'NO']
YELLOW_FINGERS = st.radio('Apakah pasien jari pasien kuning?', YELLOW_FINGERS)

AXIENTY = ['YES', 'NO']
AXIENTY = st.radio('Apakah pasien mempunyai kecemasan berlebih?', AXIENTY)

PEER_PRESSURE = ['YES', 'NO']
PEER_PRESSURE= st.radio('Apakah pasien mempunyai tekanan dari teman sebaya?', PEER_PRESSURE)

COUGHING = ['YES', 'NO']
COUGHING = st.radio('Apakah pasien batuk-batuk?', COUGHING)

SHORTNESS_OF_BREATH = ['YES', 'NO']
SHORTNESS_OF_BREATH = st.radio('Apakah pasien sesak nafas?', SHORTNESS_OF_BREATH)

SWALLOWING_DIFFICULTY = ['YES', 'NO']
SWALLOWING_DIFFICULTY = st.radio('Apakah pasien kesulitan menelan?', SWALLOWING_DIFFICULTY)

CHEST_PAIN = ['YES', 'NO']
CHEST_PAIN = st.radio('Apakah pasien nyeri dada?', CHEST_PAIN)

CHRONIC_DISEASE = ['YES', 'NO']
CHRONIC_DISEASE = st.radio('Apakah pasien mempunyai penyakit kronis?', CHRONIC_DISEASE)

WHEEZING = ['YES', 'NO']
WHEEZING = st.radio('Apakah pasien mengi (Napas Berbunyi?', WHEEZING)

predict = ''

if st.button('Estimasi '):
    predict = model.predict(
        [[AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, COUGHING, SHORTNESS OF BREATH, SWALLOWING DIFFICULTY, CHEST PAIN, CHRONIC DISEASE, WHEEZING]]
    )
    st.write('Aapakah Pasien Menderita Kanker Paru-Paru?: ', predict)
