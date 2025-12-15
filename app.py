import streamlit as st

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Deodoran Alami Berbasis IoT",
    page_icon="🌿",
    layout="wide"
)

# ===================== CUSTOM CSS =====================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

html, body {
    font-family: 'Inter', sans-serif;
}

.main {
    background-color: #F7FAF9;
}

.block-container {
    padding-top: 0;
    padding-bottom: 0;
}

/* HERO */
.hero {
    background: linear-gradient(135deg, #1E7F5C, #4FB286);
    padding: 140px 60px;
    text-align: center;
    color: white;
}

.hero h1 {
    font-size: 60px;
    font-weight: 800;
    margin-bottom: 24px;
}

.hero p {
    font-size: 22px;
    max-width: 900px;
    margin: auto;
    opacity: 0.95;
}

/* SECTION */
.section {
    padding: 110px 60px;
    background: white;
}

.section.alt {
    background: #F0F7F4;
}

.section h2 {
    font-size: 42px;
    font-weight: 700;
    color: #1E7F5C;
    margin-bottom: 30px;
}

.section p {
    font-size: 18px;
    line-height: 1.9;
    max-width: 900px;
    color: #1F2933;
}

/* BUTTON */
.btn-canva {
    display: inline-block;
    margin-top: 30px;
    padding: 16px 36px;
    font-size: 18px;
    font-weight: 600;
    border-radius: 999px;
    background: #1E7F5C;
    color: white;
    text-decoration: none;
    transition: 0.3s;
}

.btn-canva:hover {
    background: #145C43;
    transform: translateY(-2px);
}

/* FEATURE */
.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 32px;
    margin-top: 40px;
}

.feature-box {
    background: white;
    padding: 40px;
    border-radius: 32px;
    box-shadow: 0 14px 40px rgba(0,0,0,0.08);
    text-align: center;
    font-size: 18px;
}

/* FOOTER */
.footer {
    background: #145C43;
    color: white;
    text-align: center;
    padding: 60px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ===================== HERO =====================
st.markdown("""
<div class="hero">
    <h1>Deodoran Alami Berbasis IoT</h1>
    <p>
    Inovasi deodoran ramah lingkungan dari limbah sayuran hasil fermentasi
    dengan pemantauan cerdas berbasis Internet of Things
    </p>
    <a class="btn-canva" href="https://askwk.my.canva.site/deodoran-alami-berbasis-iot" target="_blank">
        🌿 Buka Website Edukasi
    </a>
</div>
""", unsafe_allow_html=True)

# ===================== SECTION 1 =====================
st.markdown("""
<div class="section">
    <h2>Tentang Produk</h2>
    <p>
    Produk ini merupakan deodoran alami berbahan limbah sayuran seperti kol,
    brokoli, dan seledri yang difermentasi secara terkontrol. Teknologi IoT
    digunakan untuk memantau parameter penting selama fermentasi agar
    kualitas produk tetap terjaga.
    </p>
</div>
""", unsafe_allow_html=True)

# ===================== SECTION 2 =====================
st.markdown("""
<div class="section alt">
    <h2>Teknologi yang Digunakan</h2>
    <div class="features">
        <div class="feature-box">📊 Sensor pH</div>
        <div class="feature-box">🌡️ Sensor Suhu & Kelembaban</div>
        <div class="feature-box">☁️ Monitoring Real-Time</div>
        <div class="feature-box">📱 Aplikasi Edukasi Android</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===================== SECTION 3 =====================
st.markdown("""
<div class="section">
    <h2>Alur Sistem</h2>
    <p>
    Limbah sayur difermentasi → dipantau oleh sensor IoT →
    data dianalisis → produk deodoran alami dihasilkan →
    informasi disebarkan melalui aplikasi edukasi dan website.
    </p>
</div>
""", unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<div class="footer">
    © 2025 Tim PKM • Deodoran Alami Berbasis IoT<br>
    Website Edukasi dibuat menggunakan Canva • Sistem IoT menggunakan Streamlit
</div>
""", unsafe_allow_html=True)
