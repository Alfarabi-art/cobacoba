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
html, body {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background-color: #f8faf9;
}

/* remove default padding */
.block-container {
    padding-top: 0;
    padding-bottom: 0;
}

/* HERO */
.hero {
    background: linear-gradient(120deg, #2e7d32, #81c784);
    padding: 120px 60px;
    border-radius: 0 0 40px 40px;
    color: white;
    text-align: center;
}
.hero h1 {
    font-size: 60px;
    font-weight: 800;
    margin-bottom: 20px;
}
.hero p {
    font-size: 22px;
    max-width: 900px;
    margin: auto;
    opacity: 0.95;
}

/* SECTION */
.section {
    padding: 100px 60px;
    background: white;
}
.section.alt {
    background: #f2f6f3;
}

.section h2 {
    font-size: 40px;
    font-weight: 700;
    color: #2e7d32;
    margin-bottom: 30px;
}
.section p {
    font-size: 18px;
    line-height: 1.9;
    max-width: 900px;
}

/* IMAGE */
.section img {
    border-radius: 30px;
}

/* FEATURE */
.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 30px;
    margin-top: 40px;
}
.feature-box {
    background: white;
    padding: 40px;
    border-radius: 30px;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.08);
    text-align: center;
}
.feature-box h3 {
    color: #2e7d32;
    margin-top: 15px;
}

/* FOOTER */
.footer {
    text-align: center;
    padding: 60px;
    background: #1b5e20;
    color: white;
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
</div>
""", unsafe_allow_html=True)

# ===================== SECTION 1 =====================
st.markdown("""
<div class="section">
    <h2>Tentang Produk</h2>
    <p>
    Produk ini merupakan deodoran alami yang dikembangkan dari limbah sayuran
    seperti kol, brokoli, dan seledri melalui proses fermentasi terkontrol.
    Proses fermentasi dipantau secara real-time menggunakan teknologi IoT
    untuk memastikan kualitas, keamanan, dan efektivitas produk.
    </p>
</div>
""", unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1542838132-92c53300491e",
    use_column_width=True
)

# ===================== SECTION 2 =====================
st.markdown("""
<div class="section alt">
    <h2>Latar Belakang</h2>
    <p>
    Deodoran berbahan kimia sintetis berpotensi menimbulkan iritasi kulit
    dan dampak lingkungan, sementara limbah sayuran terus meningkat
    tanpa pemanfaatan optimal. Inovasi ini hadir sebagai solusi
    kesehatan dan lingkungan yang berkelanjutan.
    </p>
</div>
""", unsafe_allow_html=True)

# ===================== SECTION 3 =====================
st.markdown("""
<div class="section">
    <h2>Teknologi IoT</h2>
    <div class="features">
        <div class="feature-box">
            <div style="font-size:40px">📊</div>
            <h3>Sensor pH</h3>
            <p>Memantau tingkat keasaman fermentasi secara presisi</p>
        </div>
        <div class="feature-box">
            <div style="font-size:40px">🌡️</div>
            <h3>Suhu & Kelembaban</h3>
            <p>Menjaga kondisi fermentasi tetap optimal</p>
        </div>
        <div class="feature-box">
            <div style="font-size:40px">☁️</div>
            <h3>Monitoring Real-Time</h3>
            <p>Data dipantau secara langsung berbasis IoT</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===================== SECTION 4 =====================
st.markdown("""
<div class="section alt">
    <h2>Aplikasi Edukatif Android</h2>
    <p>
    Aplikasi Android dikembangkan sebagai media edukasi
    untuk memahami proses fermentasi, pemanfaatan limbah sayur,
    serta penerapan teknologi IoT dalam kehidupan sehari-hari.
    </p>
</div>
""", unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9",
    use_column_width=True
)

# ===================== SECTION 5 =====================
st.markdown("""
<div class="section">
    <h2>Manfaat & Dampak</h2>
    <div class="features">
        <div class="feature-box">♻️ Mengurangi limbah organik</div>
        <div class="feature-box">🧴 Aman untuk kulit</div>
        <div class="feature-box">📚 Media edukasi</div>
        <div class="feature-box">🌱 Ramah lingkungan</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<div class="footer">
    © 2025 Tim Pengembang • Deodoran Alami Berbasis IoT<br>
    Program Kreativitas Mahasiswa (PKM)
</div>
""", unsafe_allow_html=True)
