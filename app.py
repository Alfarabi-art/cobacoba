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
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background-color: #f4f9f6;
}

/* HERO */
.hero {
    background: linear-gradient(120deg, #2e7d32, #66bb6a);
    padding: 80px 40px;
    border-radius: 25px;
    color: white;
    text-align: center;
    margin-bottom: 50px;
}
.hero h1 {
    font-size: 52px;
    font-weight: 800;
}
.hero p {
    font-size: 20px;
    max-width: 900px;
    margin: auto;
}

/* CARD */
.card {
    background: white;
    padding: 30px;
    border-radius: 22px;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

.card h3 {
    color: #2e7d32;
}

/* FOOTER */
.footer {
    text-align: center;
    padding: 30px;
    color: #777;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ===================== SIDEBAR =====================
st.sidebar.title("🌿 Navigasi")
menu = st.sidebar.radio(
    "Pilih Halaman",
    [
        "🏠 Beranda",
        "🌱 Tentang Produk",
        "📡 Teknologi IoT",
        "📱 Aplikasi Edukatif",
        "🌍 Manfaat & Dampak",
        "📂 Dokumentasi"
    ]
)

# ===================== PAGES =====================
if menu == "🏠 Beranda":
    st.markdown("""
    <div class="hero">
        <h1>Deodoran Alami Berbasis IoT</h1>
        <p>
        Inovasi ramah lingkungan yang mengolah limbah sayuran melalui fermentasi terkontrol
        berbasis Internet of Things
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Tentang Proyek</h3>
            <p>
            Produk ini memanfaatkan limbah sayur seperti kol, brokoli, dan seledri
            yang difermentasi untuk menghasilkan deodoran alami. Proses fermentasi
            dipantau secara real-time menggunakan teknologi IoT.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1584270354949-1b4a56e9f8fa",
            use_column_width=True
        )

elif menu == "🌱 Tentang Produk":
    st.header("🌱 Tentang Produk")
    st.markdown("""
    <div class="card">
        <p>
        Deodoran alami ini dikembangkan sebagai alternatif dari deodoran sintetis
        yang berpotensi menimbulkan iritasi kulit. Limbah sayuran yang masih
        mengandung senyawa bioaktif difermentasi untuk menghasilkan bahan
        antibakteri alami.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "📡 Teknologi IoT":
    st.header("📡 Teknologi IoT")
    col1, col2, col3 = st.columns(3)

    items = [
        ("📊 Sensor pH", "Mengontrol keasaman fermentasi"),
        ("🌡️ Sensor Suhu", "Menjaga kondisi optimal fermentasi"),
        ("☁️ Monitoring", "Pemantauan real-time berbasis IoT")
    ]

    for col, (title, desc) in zip([col1, col2, col3], items):
        with col:
            st.markdown(f"""
            <div class="card">
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

elif menu == "📱 Aplikasi Edukatif":
    st.header("📱 Aplikasi Edukatif Android")
    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.markdown("""
        <div class="card">
            <p>
            Aplikasi Android dikembangkan sebagai media edukasi masyarakat
            untuk memahami proses fermentasi, pemanfaatan limbah sayur,
            dan teknologi IoT.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9",
            use_column_width=True
        )

elif menu == "🌍 Manfaat & Dampak":
    st.header("🌍 Manfaat & Dampak")
    cols = st.columns(4)
    benefits = [
        "♻️ Mengurangi limbah organik",
        "🧴 Deodoran alami & aman",
        "📚 Media edukasi",
        "🌱 Ramah lingkungan"
    ]

    for col, text in zip(cols, benefits):
        with col:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
                <h3>{text}</h3>
            </div>
            """, unsafe_allow_html=True)

elif menu == "📂 Dokumentasi":
    st.header("📂 Dokumentasi")
    st.markdown("""
    <div class="card">
        <ul>
            <li>Dokumentasi proses fermentasi</li>
            <li>Diagram sistem IoT</li>
            <li>Hasil pemantauan sensor</li>
            <li>Modul edukasi</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<div class="footer">
    © 2025 Tim Pengembang • Deodoran Alami Berbasis IoT
</div>
""", unsafe_allow_html=True)
