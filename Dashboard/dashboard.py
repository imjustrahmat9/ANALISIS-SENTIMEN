import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Dashboard Sentimen TVRI 2024", layout="wide")

@st.cache_data
def load_data():
    file_path = os.path.join("data", "sample_dataset_tvri.csv")
    return pd.read_csv(file_path)

df = load_data()

st.title("📊 Analisis Sentimen TVRI 2024")
st.write("Dashboard ini menampilkan hasil analisis sentimen publik terhadap TVRI berdasarkan dataset yang tersedia.")

# Tampilkan data
with st.expander("Lihat Dataset"):
    st.dataframe(df.head())

# Distribusi Sentimen
st.subheader("Distribusi Sentimen")
fig, ax = plt.subplots()
sns.countplot(data=df, x="sentiment", ax=ax)
st.pyplot(fig)

# Distribusi Panjang Teks
st.subheader("Distribusi Panjang Teks")
df["text_length"] = df["text"].apply(lambda x: len(str(x).split()))
fig, ax = plt.subplots()
sns.histplot(df["text_length"], bins=30, kde=True, ax=ax)
st.pyplot(fig)

# Statistik Sentimen
st.subheader("Statistik Sentimen")
st.write(df.groupby("sentiment").agg({"text_length": "mean"}))
