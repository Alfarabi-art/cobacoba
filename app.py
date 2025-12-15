import streamlit as st

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Deodoran Alami Berbasis IoT",
    page_icon="🌿",
    layout="wide"
)

# ===================== STATE =====================
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

# ===================== CUSTOM CSS =====================
st.markdown("""
<style>
html, body {
    font-family: 'Segoe UI', sans-serif;
}
.block-container {
    padding-top: 0;
}

/* NAV BAR */
.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background: white;
    padding: 15px 60px;
    display: flex;
    justify-content: center;
    gap: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

/* NAV BUTTON */
.nav-btn button {
    background: #e8f5e9;
    border: none;
    padding: 10px 22px;
    border-radius: 30px;
    font-size: 15px;
    cursor: pointer;
    transition: 0.3s;
}
.nav-btn button:hover {
    background: #2e7d32;
    color: white;
}

/* HERO */
.hero {
    background: linear-gradient(120deg, #2e7d32, #81c784);
    padding: 120px 60px;
    color: white;
    text-align: center;
}
.hero h1 {
    font-size: 56px;
    font-weight: 800;
}

/* SECTION */
.section {
    padding: 100px 60px;
    background: white;
}
.section.alt {
    background: #f1f5f2;
}

/* FEATURE */
.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 30px;
}
.feature-box {
    background: white;
    padding: 35px;
    border-radius: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    text-align: center;
}

/* FOOTER */
.footer {
    text-align: center;
    padding: 50px;
    background: #1b5e20;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ===================== NAVIGATION =====================
st.markdown('<div class="navbar">', unsafe_allow_html=True)
cols = st.columns(6)
pages = ["Beranda", "Tentang", "IoT", "Aplikasi", "Manfaat", "Dokumentasi"]

for col, p in zip(cols, pages):
    with col:
        if st.button(p):
            st.session_state.page = p
st.markdown('</div>', unsafe_allow_html=True)

# ===================== CONTENT =====================
page = st.session_state.page

# ---------- BERANDA ----------
if page == "Beranda":
    st.markdown("""
    <div class="hero">
        <h1>Deodoran Alami Berbasis IoT</h1>
        <p>Solusi ramah lingkungan dari limbah sayuran hasil fermentasi</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- TENTANG ----------
elif page == "Tentang":
    st.markdown("""
    <div class="section">
        <h2>Tentang Produk</h2>
        <p>
        Produk ini merupakan inovasi deodoran alami berbahan limbah sayuran
        melalui fermentasi terkontrol berbasis IoT.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------- IOT ----------
elif page == "IoT":
    st.markdown("""
    <div class="section alt">
        <h2>Teknologi IoT</h2>
        <div class="features">
            <div class="feature-box">📊 Sensor pH</div>
            <div class="feature-box">🌡️ Sensor Suhu</div>
            <div class="feature-box">☁️ Monitoring Real-Time</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- APLIKASI ----------
elif page == "Aplikasi":
    st.markdown("""
    <div class="section">
        <h2>Aplikasi Edukasi Android</h2>
        <p>
        Media pembelajaran untuk mengedukasi masyarakat tentang
        fermentasi dan pemanfaatan limbah.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------- MANFAAT ----------
elif page == "Manfaat":
    st.markdown("""
    <div class="section alt">
        <h2>Manfaat</h2>
        <div class="features">
            <div class="feature-box">♻️ Kurangi limbah</div>
            <div class="feature-box">🧴 Aman</div>
            <div class="feature-box">🌱 Ramah lingkungan</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- DOKUMENTASI ----------
elif page == "Dokumentasi":
    st.markdown("""
    <div class="section">
        <h2>Dokumentasi</h2>
        <p>
        Dokumentasi sistem IoT, fermentasi, dan aplikasi edukasi.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<div class="footer">
    © 2025 Deodoran Alami Berbasis IoT | PKM
</div>
""", unsafe_allow_html=True)
