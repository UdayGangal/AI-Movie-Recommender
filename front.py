import streamlit as st
from recommender import movierecommender

recommender = movierecommender()
st.set_page_config(page_title="Movie Recommendation",layout="centered")
st.title("Movie recommender")
st.write("get similar movies based on your favorite pick")

#select box
movie_list=recommender.get_all_list()
selected_movie=st.selectbox("chose a movie",movie_list)

if st.button("recommend"):
    st.subheader("you might also like")
    recomendation=recommender.recommend(selected_movie)
    for movie in recomendation:
        st.markdown(f"you might enjoy this also:_{movie}_")