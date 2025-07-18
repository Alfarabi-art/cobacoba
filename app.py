import streamlit as st
import pandas as pd
import numpy as np
import math
import statistics

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Kalibrasi Volume",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inisialisasi halaman
if "page" not in st.session_state:
    st.session_state.page = 1

# Fungsi navigasi
def next_page():
    st.session_state.page += 1

def prev_page():
    if st.session_state.page > 1:
        st.session_state.page -= 1

# CSS Styling (tetap sama seperti punyamu)
st.markdown("""<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; color: #333; }
    .stApp { background-color: #f8f8f8; padding: 20px; }
    .header-section {
        padding: 20px 0; text-align: center;
        background-color: #F4F8D3; border-bottom: 1px solid #eee;
        margin-bottom: 30px; border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .header-section h1 { color: #5F6F65; font-weight: 700; margin: 0; }
    .hero-section {
        background: linear-gradient(to right, #CAE8BD, #B0DB9C);
        color: white; padding: 60px 30px; text-align: center;
        border-radius: 10px; margin-bottom: 40px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .hero-section h2 { font-size: 2.8em; font-weight: 700; margin-bottom: 15px; line-height: 1.2; color: white; }
    .hero-section p { font-size: 1.1em; margin-bottom: 20px; max-width: 800px; margin-left: auto; margin-right: auto; }
    .app-card {
        background-color: #ffffff; padding: 30px; border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05); margin-bottom: 30px;
    }
    .app-card h3, .app-card h4 { color: #2193b0; font-weight: 600; margin-bottom: 20px; }
    .stButton > button {
        background-color: #BAD8B6; color: white; border: none;
        padding: 10px 25px; border-radius: 5px; font-size: 1.0em;
        cursor: pointer; transition: background-color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton > button:hover {
        background-color: #E1EACD;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    </style>""", unsafe_allow_html=True)

# ------------------------
# 🔹 HALAMAN 1 (Intro)
if st.session_state.page == 1:
    st.markdown('<div class="header-section"><h1>Aplikasi Kalibrasi Volume Labu Takar</h1></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-section">
            <h2>Selamat Datang 👋</h2>
            <p>Hitung volume sebenarnya dan ketidakpastian labu takar Anda secara akurat.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="app-card"><p>Tekan "Mulai" untuk melanjutkan ke input data pengukuran.</p></div>', unsafe_allow_html=True)
    if st.button("➡ Mulai"):
        next_page()

# ------------------------
# 🔹 HALAMAN 2 (Input Data)
elif st.session_state.page == 2:
    st.markdown('<div class="header-section"><h1>Input Data Kalibrasi</h1></div>', unsafe_allow_html=True)
    v_konven = st.number_input("Masukkan Volume Konvensional (mL)", min_value=0.0, step=0.1)
    ketelitian_lb = st.number_input("Masukkan Ketelitian Labu Takar (mL)", min_value=0.0, step=0.0001, format="%.4f")

    cols = ["Bobot Kosong (g)", "Bobot Isi (g)", "Suhu Air (C)", "Suhu Udara (C)", "Tekanan Udara (mmHg)", "Kelembaban (%)"]

    if "rows" not in st.session_state:
        st.session_state.rows = 1

    def add_row(): st.session_state.rows += 1
    def remove_row(): st.session_state.rows = max(1, st.session_state.rows - 1)

    col1, col2 = st.columns(2)
    with col1: st.button(" + Tambah Baris", on_click=add_row)
    with col2: st.button(" - Hapus Baris", on_click=remove_row)

    df = st.data_editor(
        pd.DataFrame([["" for _ in cols] for _ in range(st.session_state.rows)], columns=cols),
        use_container_width=True, num_rows="dynamic"
    )

    if st.button("Hitung Rata-rata"):
        try:
            kosong = df["Bobot Kosong (g)"].astype(float).tolist()
            isi = df["Bobot Isi (g)"].astype(float).tolist()
            hasil = [b - a for a, b in zip(kosong, isi)]
            rata = {
                "Bobot Kosong (g)": sum(kosong)/len(kosong),
                "Bobot Isi (g)": sum(isi)/len(isi),
                "Bobot Isi (Hasil) (g)": sum(hasil)/len(hasil),
            }
            st.session_state.rata_pengukuran = rata
            st.success(f"Rata-rata Bobot Isi (Hasil): {rata['Bobot Isi (Hasil) (g)']:.4f} g")
        except:
            st.error("Pastikan semua data terisi dengan benar!")

    col_prev, col_next = st.columns(2)
    with col_prev:
        if st.button("⬅ Kembali"): prev_page()
    with col_next:
        if st.button("➡ Lanjut"): next_page()

# ------------------------
# 🔹 HALAMAN 3 (Hasil)
elif st.session_state.page == 3:
    st.markdown('<div class="header-section"><h1>Hasil Perhitungan</h1></div>', unsafe_allow_html=True)
    if "rata_pengukuran" in st.session_state:
        rata = st.session_state.rata_pengukuran
        st.write("📊 **Rata-rata Data**:")
        st.json(rata)

        st.markdown('<div class="app-card"><p>Perhitungan lanjutan ketidakpastian akan ditampilkan di sini.</p></div>', unsafe_allow_html=True)
    else:
        st.warning("⚠ Data belum dihitung di halaman sebelumnya.")

    if st.button("⬅ Kembali"):
        prev_page()
