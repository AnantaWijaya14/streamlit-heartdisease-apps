import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('penyakit_jantung.sav', 'rb'))

# Judul web
st.title('Prediksi Penyakit Jantung')

col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Umur')
with col2:
    sex = st.number_input('Jenis Kelamin')
with col3:
    cp = st.number_input('Jenis Nyeri Dada ')
with col1:
    trestbps = st.number_input('Tekanan Darah')
with col2:
    chol = st.number_input('Nilai Kolestrol')
with col3:
    fbs = st.number_input('Gula Darah')
with col1:
    restecg = st.number_input('Hasil Elektrokadiografi')
with col2:
    thalach = st.number_input('Detak Jantung Maksimum')
with col3:
    exang = st.number_input('Induksi Angina')
with col1:
    oldpeak = st.number_input('ST Depression')
with col2:
    slope = st.number_input('Slope')
with col3:
    ca = st.number_input('Nilai ca')
with col1:
    thal = st.number_input('Nilai Thal')

# code for prediction
heart_diagnosis = ''

# Membuat button prediksi
if st.button('Prediksi Penyakit Jantung'):
    if '' in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]:
        st.error('Semua kolom input harus diisi!')
    else:
        try:
            input_data = [
                float(age), float(sex), float(cp), float(trestbps),
                float(chol), float(fbs), float(restecg), float(thalach),
                float(exang), float(oldpeak), float(
                    slope), float(ca), float(thal)
            ]

            heart_prediction = model.predict([input_data])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
            else:
                heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
        except ValueError:
            st.error('Masukkan semua input dengan angka yang valid.')

st.success(heart_diagnosis)
