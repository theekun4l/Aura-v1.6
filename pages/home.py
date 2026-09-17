import streamlit as st

st.set_page_config(
    page_title="Aura | Home",
    page_icon="🏠",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 100px;
        animation: fadeIn 1s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Hero Section */
    .hero {
        text-align: center;
        margin-bottom: 80px;
    }

    .hero h1 {
        font-size: 64px;
        font-weight: 700;
        margin-bottom: 16px;
        letter-spacing: -1px;
    }

    .hero h1 span {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero p {
        color: #9ca3af;
        font-size: 20px;
        font-weight: 400;
    }

    /* Card-style Buttons */
    div.stButton > button {
        width: 100%;
        height: 280px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);

        font-family: Georgia, 'Times New Roman', Times, serif;
        font-size: 64px;
        font-weight: 600;
        color: white;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        z-index: 1;
    }

    div.stButton > button:hover {
        border-color: rgba(255, 255, 255, 0.3);
        background: rgba(255, 255, 255, 0.07);
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 0 0 20px rgba(79, 172, 254, 0.1);
        color: #fff;
    }

    div.stButton > button:active {
        transform: translateY(-2px) scale(1);
    }

    /* Description under buttons */
    .card-description {
        text-align: center;
        color: #9ca3af;
        font-size: 16px;
        margin-top: -120px; /* Adjusted to align with the larger buttons */
        margin-bottom: 40px;
        pointer-events: none;
        font-weight: 400;
        z-index: 2;
        position: relative;
    }

    /* Remove default streamlit button styles */
    div.stButton > button:first-child {
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)


# ---------------- HERO ----------------

st.markdown("""
<div class="hero">
    <h1>Welcome to <span>Aura</span> 👋</h1>
    <p>Your personal AI workspace</p>
</div>
""", unsafe_allow_html=True)


# ---------------- CARDS ----------------

col1, col2 = st.columns(2, gap="large")

with col1:
    if st.button("🤖\nAura", use_container_width=True):
        st.switch_page("pages/aura.py")

    st.markdown(
        '<div class="card-description">Your personal AI assistant</div>',
        unsafe_allow_html=True
    )

with col2:
    if st.button("📁\nSmart Manager", use_container_width=True):
        st.switch_page("pages/manager_page.py")

    st.markdown(
        '<div class="card-description">Scan, analyze and organize your files</div>',
        unsafe_allow_html=True
    )
