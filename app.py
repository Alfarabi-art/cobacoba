import streamlit as st

st.set_page_config(
    page_title="Deodoran Alami Berbasis IoT",
    page_icon="🌿",
    layout="wide"
)

# ===================== HIDE STREAMLIT UI =====================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container {
    padding: 0;
}
</style>
""", unsafe_allow_html=True)

# ===================== EMBED CANVA SITE =====================
st.components.v1.iframe(
    "https://askwk.my.canva.site/deodoran-alami-berbasis-iot",
    height=1500,
    scrolling=True
)
