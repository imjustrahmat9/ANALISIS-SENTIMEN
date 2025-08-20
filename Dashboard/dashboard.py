import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Config
st.set_page_config(page_title="Dashboard Sentimen TVRI 2024", layout="wide")

st.title("📊 Analisis Sentimen Komentar YouTube TVRI 2024")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/sample_dataset_tvri.csv")

df = load_data()
st.subheader("Data Preview")
st.dataframe(df.head())

# Distribusi Sentimen
st.subheader("Distribusi Sentimen")
sentiment_counts = df['sentiment'].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, ax=ax)
st.pyplot(fig)

# Wordcloud
st.subheader("Wordcloud")
text = " ".join(df['comment'])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)


