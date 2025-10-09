# Bike Sharing Dashboard

Dashboard interaktif untuk menganalisis pola penggunaan penyewaan sepeda berdasarkan data harian dan per jam (2011–2012).  
Dibangun menggunakan **Streamlit**, **Pandas**, **Matplotlib**, dan **Seaborn**.

---

## Fitur Dashboard

- **Visualisasi tren penyewaan** sepeda harian dan per jam
- **Analisis musiman** berdasarkan musim, cuaca, dan hari dalam seminggu
- **Perbandingan pengguna casual vs registered**
- **Filter rentang tanggal** melalui sidebar

---

## Persyaratan

Pastikan sudah menginstal:

- Python ≥ 3.9
- pip (package manager)

---

## ⚙️ Instalasi

1. **Extract file ZIP**
2. **Buka terminal, lalu arahkan ke folder hasil ekstraksi**

   ```bash
   cd "path_ke_folder/Data Analysis with Python"
   ```

3. **Buat virtual environment (opsional tapi disarankan)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # untuk macOS/Linux
   venv\Scripts\activate      # untuk Windows
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶Menjalankan Dashboard Secara Lokal

1. Jalankan perintah berikut:

   ```bash
   streamlit run app.py
   ```

2. Streamlit akan otomatis membuka browser di:

   ```
   http://localhost:8501
   ```

3. Gunakan sidebar untuk memilih rentang tanggal dan melihat berbagai visualisasi.

---

## Dibuat oleh

**Muhammad Anang Mahrub**
