import streamlit as st
from recommender import movierecommender

# Page Config

st.set_page_config(
    page_title="🎬 Movie Matchmaker",
    layout="centered",
    initial_sidebar_state="collapsed"
)

#CSS 
bg_url = "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;500;700&display=swap');

    .stApp {{
        background-image: url('{bg_url}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(20, 20, 30, 0.8);
        z-index: -1;
    }}

    html, body, [class*="css"] {{
        font-family: 'Montserrat', sans-serif;
        color: #F5F5F5;
    }}

    h1 {{
        font-weight: 700;
        font-size: 3rem;
        text-align: center;
        color: #D4AF37;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }}

    p.subtitle {{
        text-align: center;
        font-weight: 300;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        color: #E0E0E0;
    }}

    .stButton>button {{
        background-color: #800000;
        color: #F5F5F5;
        font-weight: 500;
        letter-spacing: 0.5px;
        padding: 12px 30px;
        border-radius: 8px;
        transition: 0.3s ease;
        margin-top: 10px;
    }}

    .stButton>button:hover {{
        background-color: #A52A2A;
        box-shadow: 0 0 8px #D4AF37;
    }}

    .movie-box {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 12px 16px;
        margin-bottom: 10px;
        border-left: 4px solid #D4AF37;
        border-radius: 8px;
        font-style: italic;
        color: #F5F5F5;
    }}

    .main-container {{
        padding: 2rem;
        backdrop-filter: blur(3px);
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        margin: auto;
        max-width: 700px;
    }}
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    
    st.markdown("<h1>🎞️ Movie Matchmaker</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Find your next favorite film based on one you love 🍿</p>", unsafe_allow_html=True)

    
    recommender = movierecommender()
    movie_list = recommender.get_all_titles()

    selected_movie = st.selectbox("🎬 Choose a movie", movie_list)

    if st.button("🎯 Recommend"):
        st.markdown("### 🎥 You might enjoy:")
        recommendations = recommender.recommend(selected_movie)
        for movie in recommendations:
            st.markdown(f"<div class='movie-box'>🎬 {movie}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
