# 📊 Dashboard Analisis Sentimen Komentar YouTube TVRI 2024

Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis komentar penonton di kanal YouTube TVRI tahun 2024.  
Analisis meliputi *data cleaning*, *sentiment classification* (positif, netral, negatif), visualisasi distribusi, wordcloud, filter komentar, hingga evaluasi model (classification report & confusion matrix)
---

## 🚀 Fitur Utama
- 📂 **Upload Dataset** (format `.csv` atau `.xlsx`).
- 👀 **Preview Data** (tampilkan beberapa baris komentar).
- 📊 **Distribusi Sentimen** dalam bentuk tabel & grafik batang.
- ☁️ **Wordcloud** kata-kata dominan dalam komentar.
- 🔍 **Filter Komentar** berdasarkan kategori sentimen.
- 📈 **Evaluasi Model** *(jika dataset memiliki kolom `true_label`)*:
  - Classification report (Precision, Recall, F1-score).
  - Confusion Matrix (heatmap).
- 💾 **Download Hasil Analisis** dalam format CSV.

---

## 📦 Instalasi & Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/username/analisis-sentimen-tvri2024.git
cd analisis-sentimen-tvri2024
```

### 2. Install Dependencies
Pastikan Python 3.8+ sudah terpasang.  
Kemudian install requirements:
```bash
pip install -r requirements.txt
```

Jika `requirements.txt` belum ada, gunakan:
```bash
pip install streamlit pandas matplotlib seaborn wordcloud scikit-learn openpyxl
```

### 3. Jalankan Aplikasi
```bash
streamlit run app.py
```

---

## 📂 Struktur Project
```
├── app.py                       # Aplikasi Streamlit utama
├── sample_sentimen_tvri.csv     # Dataset contoh
├── README.md                    # Dokumentasi project
└── requirements.txt             # (opsional) daftar dependensi
```

---

## 📊 Contoh Dataset
File contoh `sample_sentimen_tvri.csv`:

```csv
comment,sentiment,true_label
"TVRI sekarang jauh lebih bagus tayangannya","Positif","Positif"
"Acara ini membosankan sekali","Negatif","Negatif"
"Informasinya cukup jelas, netral saja menurut saya","Netral","Netral"
"Terima kasih TVRI, sangat bermanfaat","Positif","Positif"
```

- **comment** = teks komentar dari YouTube.  
- **sentiment** = label hasil analisis otomatis (*Positif, Netral, Negatif*).  
- **true_label** = label sebenarnya (jika ada, digunakan untuk evaluasi model).  

---

## 📈 Hasil Visualisasi
1. Distribusi Sentimen  
   ![sentiment_distribution](docs/sentiment_bar.png)

2. Wordcloud  
   ![wordcloud](docs/wordcloud.png)

3. Confusion Matrix  
   ![confusion_matrix](docs/confusion_matrix.png)

---

## 🤝 Kontribusi
Pull request dipersilakan. Untuk perubahan besar, mohon buka *issue* terlebih dahulu untuk membahas apa yang ingin diubah.

---

## 📜 Lisensi
[MIT License](LICENSE)
