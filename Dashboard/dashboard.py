import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Fungsi load data dengan path relatif
@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)  # lokasi file dashboard.py
    file_path = os.path.join(base_path, "../data/sample_dataset_tvri.csv")
    return pd.read_csv(file_path)

# Load data
df = load_data()

# Judul
st.title("📊 Analisis Sentimen TVRI")

# Preview data
st.subheader("🔍 Data Awal")
st.dataframe(df.head())

# Statistik sederhana
st.subheader("📈 Statistik Data")
st.write(df.describe())

# Visualisasi Sentimen
st.subheader("📊 Distribusi Sentimen")
if "sentimen" in df.columns:
    fig, ax = plt.subplots()
    sns.countplot(x="sentimen", data=df, ax=ax)
    st.pyplot(fig)
else:
    st.warning("Kolom 'sentimen' tidak ditemukan di dataset.")



