import streamlit as st
from recommender import movierecommender

# Setup page config
st.set_page_config(
    page_title="🎬 Movie Matchmaker",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for movie-style aesthetics
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500&family=Roboto+Mono&display=swap');

    html, body, [class*="css"]  {
        background-color: #0f0f0f;
        color: #f0f0f0;
        font-family: 'Roboto Mono', monospace;
    }
    h1 {
        color: #ff4c4c;
        font-family: 'Oswald', sans-serif;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 0;
    }
    .stSelectbox > div {
        background-color: #1c1c1c !important;
        border: 1px solid #444 !important;
        color: white !important;
    }
    .stButton>button {
        background-color: #ff4c4c;
        color: white;
        font-weight: bold;
        padding: 10px 24px;
        border-radius: 8px;
        margin-top: 15px;
    }
    .movie-box {
        background-color: #1a1a1a;
        padding: 10px 15px;
        margin-bottom: 10px;
        border-left: 4px solid #ff4c4c;
        font-style: italic;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)
