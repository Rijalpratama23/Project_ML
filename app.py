import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analisis Penjualan", layout="wide")
st.title("📊 Visualisasi Jumlah Penjualan per Produk🧐")

# Opsi metode input data
input_mode = st.radio("Pilih metode input data:", ["Upload File Excel", "Input Manual"])

df = None

if input_mode == "Upload File Excel":
    uploaded_file = st.file_uploader("Unggah file Excel (.xlsx)", type=["xlsx"])
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file, sheet_name='data_penjualan')
            st.success("✅ File berhasil dibaca.")
        except Exception as e:
            st.error(f"❌ Gagal membaca file: {e}")

elif input_mode == "Input Manual":
    st.info("Silakan input data secara manual.")
    # Tabel kosong yang bisa diedit user
    manual_data = st.data_editor(
        pd.DataFrame({
            'Produk': ['Produk A', 'Produk B'],
            'Jumlah': [10, 15]
        }),
        num_rows="dynamic",
        use_container_width=True
    )
    df = manual_data

# Jika data sudah tersedia, lakukan proses selanjutnya
if df is not None:
    st.subheader("📋 Data Penjualan")
    st.dataframe(df)

    # Normalisasi nama kolom
    df.columns = df.columns.str.strip().str.lower()

    # Ganti nama kolom jika perlu
    if 'nama produk' in df.columns:
        df.rename(columns={'nama produk': 'produk'}, inplace=True)
    if 'jumlah terjual' in df.columns:
        df.rename(columns={'jumlah terjual': 'jumlah'}, inplace=True)

    # Visualisasi
    if 'produk' in df.columns and 'jumlah' in df.columns:
        st.subheader("📊 Grafik Penjualan")
        plt.figure(figsize=(10, 5))
        sns.barplot(data=df, x='produk', y='jumlah')
        plt.xticks(rotation=45)
        plt.title("Jumlah Penjualan per Produk")
        st.pyplot(plt)
    else:
        st.warning("❌ Kolom 'produk' dan 'jumlah' belum ditemukan.")
