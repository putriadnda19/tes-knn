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

SHORTNESSOFBREATH= ['YES', 'NO']
SHORTNESSOFBREATH = st.radio('Apakah pasien sesak nafas?', SHORTNESSOFBREATH)



predict = ''

if st.button('Estimasi '):
    st.write('Aapakah Pasien Menderita Kanker Paru-Paru?: ', predict)
