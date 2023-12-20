import pickle 
import streamlit as st 

st.title('Estimasi Pasien Yang Menderita Kanker Paru-Paru')

AGE = st.number_input('Input umur pasien')
TotalFat = st.radio('Apakah pasien jari pasien kuning?')

st.write("Anda memilih", genre)

genre = st.radio(
    "Apakah pasien jari pasien kuning?",
    ["YES", "NO"],
    index=None,
)

st.write("Anda memilih", genre)

genre = st.radio(
    "Apakah pasien mempunyai kecemasan berlebih?",
    ["YES", "NO"],
    index=None,
)

st.write("Anda memilih", genre)

genre = st.radio(
    "Apakah pasien mempunyai tekanan dari teman sebaya?",
    ["YES", "NO"],
    index=None,
)

st.write("Anda memilih", genre)

genre = st.radio(
    "Apakah pasien batuk-batuk?",
    ["YES", "NO"],
    index=None,
)

st.write("Anda memilih", genre)

genre = st.radio(
    "Apakah pasien sesak nafas?",
    ["YES", "NO"],
    index=None,
)

st.write("Anda memilih", genre)

genre = st.radio(
    "Apakah pasien kesulitan menelan?",
    ["YES", "NO"],
    index=None,
)

st.write("Anda memilih", genre)

genre = st.radio(
    "Apakah pasien nyeri dada?",
    ["YES", "NO"],
    index=None,
)

st.write("Anda memilih", genre)

genre = st.radio(
    "Apakah pasien mempunyai penyakit kronis?",
    ["YES", "NO"],
    index=None,
)

st.write("Anda memilih", genre)

genre = st.radio(
    "Apakah pasien mengi (Napas Berbunyi?",
    ["YES", "NO"],
    index=None,
)

st.write("Anda memilih", genre)


predict = ''

if st.button('Estimasi '):
    st.write('Aapakah Pasien Menderita Kanker Paru-Paru?: ', predict)
