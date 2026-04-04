# 🚀 MLOps - Accident Risk Prediction (Los Angeles)

## 📌 Deskripsi Proyek
Proyek ini merupakan implementasi sistem MLOps untuk prediksi risiko kecelakaan lalu lintas berbasis data time-series. Dataset yang digunakan adalah US Accidents (2016–2023) dari Kaggle, dengan fokus pada wilayah Los Angeles.

Sistem ini dirancang untuk mensimulasikan data dinamis menggunakan pendekatan pembagian data berbasis waktu (bulanan), sehingga mendukung konsep Continual Learning.

---

## ⚙️ Arsitektur Pipeline

Pipeline yang dibangun:

Kaggle Dataset → data/raw → ingestion → batch data → preprocessing → data/processed

---

## 🔄 Data Ingestion (Dinamis)

Data diambil dari dataset statis dan disimulasikan menjadi dinamis dengan cara:
- Membagi data berdasarkan waktu (Start_Time)
- Mengambil data per bulan
- Menyimpan hasil sebagai batch baru

Contoh output:
data/raw/batch/accidents_2016-06.csv

Setiap eksekusi menghasilkan file baru (tidak overwrite).

---

## 🧹 Data Preprocessing

Tahapan preprocessing meliputi:
- Filtering data berdasarkan lokasi (Los Angeles)
- Konversi tipe data waktu
- Penyimpanan ke folder data/processed/

Output:
data/processed/los_angeles_accidents.csv

---

## 📁 Struktur Direktori

MLOps-Accident-Risk-Prediction/
│
├── data/
│   ├── raw/
│   │   └── batch/
│   ├── processed/
│
├── src/
│   └── data/
│       ├── ingest_data.py
│       ├── load_data.py
│       ├── preprocess.py
│
├── scripts/
│   └── run_pipeline.py
│
├── README.md
└── .gitignore

---

## ▶️ Cara Menjalankan

1. Data Ingestion (Simulasi Dinamis)
python -m src.data.ingest_data

2. Preprocessing
python -m src.data.preprocess

3. Full Pipeline
python -m scripts.run_pipeline

---

## 🧠 Konsep Utama

- Data Dinamis (Simulasi): Data dibagi per bulan untuk mensimulasikan aliran data bertahap
- Reproducibility: Pipeline dapat dijalankan ulang dengan hasil konsisten
- Modular Code: Setiap proses dipisah (ingestion, preprocessing, pipeline)
- MLOps Ready: Siap dikembangkan ke tahap machine learning

---

## 📊 Dataset

Sumber:
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

---

## ✨ Kesimpulan

Proyek ini berhasil mengimplementasikan pipeline data MLOps dengan:
- Data ingestion dinamis (simulasi)
- Automasi preprocessing
- Struktur modular dan scalable

Sistem ini siap dikembangkan ke tahap machine learning dan continual learning.