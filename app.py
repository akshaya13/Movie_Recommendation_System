import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=<<Key>>'.format(movie_id))  #repalce <<key>> with your api key
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    output_posters = []
    for i in movies_list[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
        # print(i[0]) this is the local movie numbers (1 to 5000)
        fetch_poster(movies.iloc[i[0]].id)
        output_posters.append(fetch_poster(movies.iloc[i[0]].id))

    return recommended_movies, output_posters


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie = st.selectbox(
    "How would you like to be contacted?",
    # ("Email", "Home phone", "Mobile phone"))
    movies['title'].values)

st.write("You selected:", selected_movie)

if st.button('Recommend'):
    rec, posters = recommend(selected_movie)
    # for i in recommendations:
    #     st.write(i)
    ###################################################################

    # Create 5 columns dynamically
    cols = st.columns(5)

    # Iterate over each recommendation and poster
    for i in range(5):
        with cols[i]:
            st.text(rec[i])
            st.image(posters[i])
    # ###################################################################
    #  # containers/Tile
    # row1 = st.columns(3)
    # row2 = st.columns(2)
    # for i in posters, rec:
    #     for col in row1 + row2:
    #         tile = col.container(height=220)
    #         tile.title(rec[i])
    #         tile.image(posters[i])

