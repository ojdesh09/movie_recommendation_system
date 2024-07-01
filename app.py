import pickle
import streamlit as st
import requests

# Custom CSS for dark theme and better font
st.markdown(
    """
    <style>
    body {
        background-color: #2E2E2E;
        color: white;
        font-family: 'Helvetica', sans-serif;
    }
    .stTextInput, .stButton>button {
        background-color: #333333;
        color: white;
    }
    .stTextInput>div>div>input {
        color: white;
    }
    .stTextInput>div>div>label {
        color: white;
    }
    .stSelectbox div[data-baseweb="select"] {
        background-color: #333333;
        color: white;
    }
    .stSelectbox div[data-baseweb="select"]>div {
        border-color: #666666;
    }
    .stButton>button {
        border: 1px solid #666666;
        box-shadow: none;
        font-size: 14px;
    }
    .stButton>button:hover {
        border: 1px solid #FFFFFF;
        background-color: #444444;
    }
    .css-1d391kg {
        color: #FFFFFF;
    }
    .css-1d391kg:hover {
        color: #D3D3D3;
    }
    .stImage>div>img {
        border-radius: 10px;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Helvetica', sans-serif;
    }
    h1 {
        font-size: 28px;
    }
    h2 {
        font-size: 24px;
    }
    h3 {
        font-size: 20px;
    }
    h4 {
        font-size: 16px;
    }
    h5 {
        font-size: 14px;
    }
    h6 {
        font-size: 12px;
    }
    .stMarkdown {
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Header and title
st.header('Movie Recommender System')
st.markdown("<h2 style='text-align: center; color: white;'>Find Your Next Favorite Movie</h2>", unsafe_allow_html=True)

# Load movies and similarity matrices
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Show recommendations on button click
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        if i < len(recommended_movie_names):
            with col:
                st.markdown(f"<h4 style='text-align: center;'>{recommended_movie_names[i]}</h4>", unsafe_allow_html=True)
                st.image(recommended_movie_posters[i], use_column_width=True)
