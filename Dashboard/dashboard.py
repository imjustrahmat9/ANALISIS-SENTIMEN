pip install -r requirements.txt

# dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from textblob import TextBlob
import io

# -------------------------------
# Konfigurasi Halaman
# -------------------------------
st.set_page_config(page_title="Dashboard Sentimen TVRI 2024", layout="wide")
st.title("📊 Dashboard Analisis Sentimen YouTube TVRI 2024")

# -------------------------------
# Upload Dataset
# -------------------------------
uploaded_file = st.file_uploader("📂 Upload Dataset (Excel/CSV)", type=["xlsx", "csv"])

if uploaded_file is not None:
    # Baca dataset
    if uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)

    st.subheader("📌 Preview Data")
    st.dataframe(df.head())

    # -------------------------------
    # Data Cleaning
    # -------------------------------
    st.subheader("🧹 Data Cleaning")
    df = df.dropna().drop_duplicates()
    df["cleaned_text"] = df["Komentar"].astype(str).str.lower()

    st.write("Jumlah komentar setelah cleaning:", len(df))

    # -------------------------------
    # Sentiment Labeling
    # -------------------------------
    st.subheader("🔎 Sentiment Labeling (TextBlob)")
    def get_sentiment(text):
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0:
            return "positive"
        elif polarity < 0:
            return "negative"
        else:
            return "neutral"

    df["sentiment"] = df["cleaned_text"].apply(get_sentiment)
    st.dataframe(df[["Komentar", "sentiment"]].head(10))

    # -------------------------------
    # Distribusi Sentimen
    # -------------------------------
    st.subheader("📊 Distribusi Sentimen")
    fig, ax = plt.subplots()
    sns.countplot(x="sentiment", data=df, ax=ax, palette="Set2")
    st.pyplot(fig)

    # -------------------------------
    # WordCloud
    # -------------------------------
    st.subheader("☁️ WordCloud")
    text = " ".join(df["cleaned_text"])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

    # -------------------------------
    # TF-IDF + PCA
    # -------------------------------
    st.subheader("📐 TF-IDF + PCA")
    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(df["cleaned_text"]).toarray()

    pca = PCA(n_components=100)
    X_pca = pca.fit_transform(X)

    st.write("Shape TF-IDF:", X.shape)
    st.write("Shape PCA:", X_pca.shape)

    # -------------------------------
    # Modeling (Naive Bayes & SVM)
    # -------------------------------
    st.subheader("🤖 Modeling (Naive Bayes & SVM)")
    y = df["sentiment"]

    model_nb = GaussianNB()
    model_nb.fit(X_pca, y)
    y_pred_nb = model_nb.predict(X_pca)

    model_svm = SVC(kernel="linear")
    model_svm.fit(X_pca, y)
    y_pred_svm = model_svm.predict(X_pca)

    # Tampilkan Hasil
    st.write("### Naive Bayes Classification Report")
    st.text(classification_report(y, y_pred_nb))

    st.write("### SVM Classification Report")
    st.text(classification_report(y, y_pred_svm))

    # Confusion Matrix
    st.write("### Confusion Matrix (SVM)")
    cm = confusion_matrix(y, y_pred_svm, labels=["positive", "neutral", "negative"])
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["positive","neutral","negative"], yticklabels=["positive","neutral","negative"], ax=ax)
    st.pyplot(fig)

else:
    st.info("⬆️ Silakan upload file dataset terlebih dahulu untuk memulai analisis.")

