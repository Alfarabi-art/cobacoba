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
/* Global */
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background-color: #f6faf7;
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, #4CAF50, #2E7D32);
    padding: 60px 40px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 50px;
}

.hero h1 {
    font-size: 48px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    opacity: 0.95;
}

/* Card */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

/* Section Title */
.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #2E7D32;
    margin-bottom: 15px;
}

/* List */
ul {
    padding-left: 20px;
}
li {
    margin-bottom: 8px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 30px;
    color: #666;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ===================== HERO =====================
st.markdown("""
<div class="hero">
    <h1>🌿 Deodoran Alami Berbasis IoT</h1>
    <p>Inovasi ramah lingkungan dari limbah sayur dengan pemantauan fermentasi secara real-time</p>
</div>
""", unsafe_allow_html=True)

# ===================== CONTENT =====================
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="section-title">Apa Itu Produk Ini?</div>
        <p>
        Produk ini merupakan deodoran alami yang dibuat dari limbah sayuran hasil fermentasi
        seperti kol, brokoli, dan seledri. Proses fermentasi dipantau menggunakan teknologi
        Internet of Things (IoT) untuk memastikan kualitas dan keamanan produk.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image(
        "https://via.placeholder.com/450x350.png?text=Deodoran+Alami",
        use_column_width=True
    )

# ===================== WHY IMPORTANT =====================
st.markdown("""
<div class="card">
    <div class="section-title">Mengapa Ini Penting?</div>
    <p>
    Deodoran berbahan kimia sintetis berpotensi menimbulkan iritasi kulit dan dampak lingkungan.
    Di sisi lain, limbah sayuran terus meningkat dan belum dimanfaatkan secara optimal.
    Inovasi ini menghadirkan solusi yang aman, berkelanjutan, dan edukatif.
    </p>
</div>
""", unsafe_allow_html=True)

# ===================== TECHNOLOGY =====================
st.markdown("""
<div class="card">
    <div class="section-title">Teknologi IoT yang Digunakan</div>
    <ul>
        <li>Sensor pH untuk memantau tingkat keasaman fermentasi</li>
        <li>Sensor suhu dan kelembapan untuk menjaga kondisi optimal</li>
        <li>Monitoring real-time berbasis Internet of Things (IoT)</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ===================== EDUCATION =====================
st.markdown("""
<div class="card">
    <div class="section-title">Aplikasi Edukatif Android</div>
    <p>
    Aplikasi Android dikembangkan sebagai media edukasi untuk masyarakat, berisi
    panduan pengolahan limbah sayur, penjelasan fermentasi, serta visualisasi data
    sensor secara real-time.
    </p>
</div>
""", unsafe_allow_html=True)

# ===================== BENEFITS =====================
st.markdown("""
<div class="card">
    <div class="section-title">Manfaat Produk</div>
    <ul>
        <li>Mengurangi limbah organik rumah tangga</li>
        <li>Deodoran alami yang aman untuk kulit</li>
        <li>Meningkatkan kesadaran lingkungan</li>
        <li>Sarana edukasi sains dan teknologi</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<div class="footer">
    © 2025 Tim Pengembang • Deodoran Alami Berbasis IoT
</div>
""", unsafe_allow_html=True)
