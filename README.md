# MLOps Accident Risk Prediction

## Project Overview

Proyek ini merupakan implementasi awal dari pipeline **Machine Learning Operations (MLOps)** untuk memprediksi tingkat risiko kecelakaan berdasarkan berbagai fitur yang berkaitan dengan kondisi pengemudi, kendaraan, dan lingkungan.

Tujuan utama proyek ini adalah membangun **fondasi teknis proyek machine learning yang reproducible dan terstandarisasi**, sehingga eksperimen, pengembangan model, dan deployment dapat dilakukan secara konsisten oleh siapa pun yang bekerja pada repositori ini.

Repositori ini juga dirancang untuk mengikuti praktik terbaik dalam pengembangan proyek machine learning modern, seperti:

* penggunaan **GitHub Codespaces** untuk lingkungan pengembangan yang konsisten,
* penerapan **GitHub Flow** untuk manajemen branch dan eksperimen,
* penggunaan **struktur direktori standar industri** untuk proyek data science.

Pada tahap awal ini, proyek difokuskan pada:

* menyiapkan struktur proyek machine learning,
* melakukan eksplorasi data awal (Exploratory Data Analysis / EDA),
* membangun fondasi pipeline pengolahan data dan pelatihan model.

---

# Project Objectives

Beberapa tujuan dari proyek ini antara lain:

1. Membangun sistem prediksi risiko kecelakaan berbasis machine learning.
2. Menerapkan praktik **MLOps** untuk memastikan proses pengembangan model dapat direproduksi.
3. Menyediakan struktur proyek yang modular sehingga mudah dikembangkan.
4. Memisahkan komponen data, fitur, model, dan inference secara jelas.
5. Menggunakan GitHub sebagai pusat manajemen kode dan eksperimen.

---

# Repository URL

Repositori proyek dapat diakses melalui:

https://github.com/bagrah/MLOps-Accident-Risk-Prediction

---

# Development Environment

Proyek ini menggunakan **GitHub Codespaces** sebagai lingkungan pengembangan utama.

Codespaces memungkinkan developer menjalankan proyek secara langsung di cloud tanpa perlu melakukan instalasi lokal.

Keuntungan menggunakan Codespaces:

* lingkungan Python sudah terkonfigurasi
* dependency dapat diinstal secara otomatis
* proyek dapat dijalankan di perangkat mana pun
* memudahkan kolaborasi tim

---

# How to Run the Project using GitHub Codespaces

Ikuti langkah berikut untuk menjalankan proyek ini menggunakan Codespaces:

### 1. Buka Repository

Masuk ke halaman repository GitHub:

https://github.com/bagrah/MLOps-Accident-Risk-Prediction

### 2. Jalankan Codespaces

Klik tombol:

Code → Codespaces → Create codespace on main

GitHub akan membuat environment development berbasis cloud.

### 3. Tunggu Environment Siap

Codespaces akan memuat:

* VS Code environment
* Python interpreter
* terminal workspace

### 4. Install Dependencies

Jalankan perintah berikut pada terminal:

pip install -r requirements.txt

Library utama yang digunakan:

* pandas
* numpy
* scikit-learn
* matplotlib
* jupyter

### 5. Jalankan Notebook

Buka folder:

notebooks

Lalu jalankan file:

eda.ipynb

Notebook ini digunakan untuk melakukan **exploratory data analysis (EDA)** pada dataset kecelakaan.

---

# Project Structure

Repositori ini menggunakan struktur proyek machine learning yang mengikuti praktik industri.

```
MLOps-Accident-Risk-Prediction
│
├── data
│   ├── raw
│   │   └── dataset asli
│   │
│   └── processed
│       └── dataset yang sudah diproses
│
├── notebooks
│   └── eda.ipynb
│
├── src
│   ├── data
│   │   ├── load_data.py
│   │   └── preprocess.py
│   │
│   ├── features
│   │   └── build_features.py
│   │
│   ├── models
│   │   ├── train_model.py
│   │   └── evaluate_model.py
│   │
│   └── inference
│       └── predict.py
│
├── tests
│   └── test_model.py
│
├── configs
│   └── config.yaml
│
├── scripts
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Explanation of Each Folder

### data/

Folder ini digunakan untuk menyimpan dataset proyek.

* **raw/**
  Berisi dataset asli yang belum diproses.

* **processed/**
  Berisi dataset yang sudah melalui tahap preprocessing.

---

### notebooks/

Folder ini berisi notebook eksplorasi data.

Notebook digunakan untuk:

* eksplorasi dataset
* visualisasi data
* eksperimen awal model

---

### src/

Folder ini berisi kode utama proyek machine learning.

Struktur di dalamnya dipisahkan berdasarkan fungsi pipeline.

#### src/data/

Digunakan untuk proses loading dan preprocessing data.

Contoh:

* membaca dataset
* membersihkan data
* transformasi awal

#### src/features/

Digunakan untuk proses **feature engineering**, yaitu membangun fitur yang lebih informatif dari data mentah.

#### src/models/

Berisi kode untuk proses machine learning seperti:

* training model
* evaluasi model

#### src/inference/

Digunakan untuk melakukan prediksi menggunakan model yang sudah dilatih.

---

### tests/

Folder ini digunakan untuk menulis unit test agar kode tetap stabil saat proyek berkembang.

---

### configs/

Folder ini menyimpan konfigurasi proyek seperti:

* parameter model
* lokasi dataset
* konfigurasi pipeline

---

### scripts/

Folder ini dapat digunakan untuk menyimpan script tambahan seperti:

* automation
* pipeline execution
* data pipeline

---

# Branching Strategy (GitHub Flow)

Repositori ini menggunakan **GitHub Flow** sebagai strategi pengelolaan kode.

Langkah workflow:

1. Membuat branch baru dari `main`
2. Mengembangkan fitur atau eksperimen pada branch tersebut
3. Melakukan commit perubahan
4. Membuat Pull Request
5. Melakukan merge ke branch `main` setelah validasi

Contoh branch pada proyek ini:

```
feat/initial-eda
```

Branch ini digunakan untuk melakukan eksplorasi data awal sebelum pengembangan model machine learning.

---

# Initial Experiment

Eksperimen awal dilakukan menggunakan notebook:

```
notebooks/eda.ipynb
```

Notebook ini digunakan untuk:

* memahami struktur dataset
* melakukan eksplorasi fitur
* mengidentifikasi pola awal pada data kecelakaan.

---

# Future Development

Pengembangan selanjutnya dari proyek ini akan mencakup:

* feature engineering lanjutan
* training model machine learning
* evaluasi performa model
* implementasi pipeline MLOps
* deployment model untuk inference

---

# License

Proyek ini menggunakan lisensi **MIT License** yang memungkinkan penggunaan dan pengembangan ulang secara bebas dengan tetap mencantumkan atribusi kepada pengembang asli.
