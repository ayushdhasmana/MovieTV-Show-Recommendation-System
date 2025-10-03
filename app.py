
import pickle
import streamlit as st
import pandas as pd

# Load pickled data
movies = pickle.load(open('movies.pkl', 'rb'))   # DataFrame
similarity = pickle.load(open('similarity.pkl', 'rb'))  # similarity matrix

# Recommendation function
def recommend(title, n=5):
    if title not in movies['Title'].values:
        return ["Title not found"]
    idx = movies[movies['Title'] == title].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    recommendations = movies['Title'].iloc[[i[0] for i in sim_scores]]
    return recommendations.tolist()

# Streamlit UI
st.title('🎬 Movie Recommender System')

# Dropdown (select box)
selected_movie_name = st.selectbox(
    'Choose a movie you like:',
    movies['Title'].values
)

# Button
if st.button('Recommend'):
    recs = recommend(selected_movie_name)
    st.write("**Recommended Movies:**")
    for r in recs:
        st.write(r)

