import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analisis Penjualan", layout="wide")

st.title("📊 Visualisasi Jumlah Penjualan per Produk🧐")

uploaded_file = st.file_uploader("Unggah file Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    try:
        # Membaca sheet bernama 'data_penjualan'
        df = pd.read_excel(uploaded_file, sheet_name='data_penjualan')
        
        st.subheader("📋 Daftar Kolom dalam File")
        st.write(df.columns.tolist())  # Tampilkan nama kolom untuk membantu debugging

        st.subheader("🧾 Data Penjualan")
        st.dataframe(df)

        st.subheader("📈 Visualisasi Jumlah Penjualan per Produk")

        # Normalisasi nama kolom (strip spasi, ubah ke lowercase)
        df.columns = df.columns.str.strip().str.lower()

        # Ganti nama kolom jika diperlukan (bisa kamu sesuaikan)
        if 'nama produk' in df.columns:
            df.rename(columns={'nama produk': 'produk'}, inplace=True)
        if 'jumlah terjual' in df.columns:
            df.rename(columns={'jumlah terjual': 'jumlah'}, inplace=True)

        # Cek apakah kolom 'produk' dan 'jumlah' sudah tersedia
        if 'produk' in df.columns and 'jumlah' in df.columns:
            plt.figure(figsize=(10, 5))
            sns.barplot(data=df, x='produk', y='jumlah')
            plt.xticks(rotation=45)
            plt.title("Jumlah Penjualan per Produk")
            st.pyplot(plt)
        else:
            st.error("❌ Kolom 'produk' atau 'jumlah' tidak ditemukan dalam file Excel. Harap pastikan nama kolom sudah benar.")

    except Exception as e:
        st.error(f"❌ Terjadi kesalahan saat membaca file: {e}")
