import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Analisis Data Penjualan")

# Upload file
uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded_file is not None:
    try:
        # Membaca file Excel dan sheet tertentu
        df = pd.read_excel(uploaded_file, sheet_name='data_penjualan')

        st.subheader("📊 Data Penjualan")
        st.write(df)

        # Contoh visualisasi: jumlah penjualan per produk
        st.subheader("📈 Visualisasi Jumlah Penjualan per Produk")
        plt.figure(figsize=(10, 5))
        sns.barplot(data=df, x='produk', y='jumlah')
        plt.xticks(rotation=45)
        st.pyplot(plt)

    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
else:
    st.info("Silakan upload file Excel (.xlsx) yang berisi sheet 'data_penjualan'.")
