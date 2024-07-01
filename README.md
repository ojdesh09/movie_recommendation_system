# Movie Recommendation System

## Overview
This project implements a movie recommendation system using collaborative filtering. It recommends movies similar to the one selected by the user based on movie similarity matrices computed from user ratings.

## Libraries Used
- **Streamlit**: Used for building the web application interface that allows users to select a movie and view recommendations.
- **Pickle**: Utilized to serialize and deserialize Python objects, specifically for loading precomputed movie data and similarity matrices.
- **Requests**: Used for making HTTP requests to The Movie Database (TMDb) API to fetch movie details and posters dynamically.

## Model
The recommendation system employs collaborative filtering, a widely used technique in recommendation engines. Here’s how the model works:

- **Data Preparation**: Movie ratings data is used to construct a movie-user matrix, where rows represent movies and columns represent users.
- **Similarity Calculation**: Similarity between movies is computed using metrics like cosine similarity or Pearson correlation based on their user ratings.
- **Recommendation Generation**: For a selected movie, the system identifies similar movies based on computed similarity scores and recommends the top matches.

## Features
- **Movie Selection**: Users can select a movie from a dropdown menu populated with a list of available movies.
- **Recommendation Display**: Upon selecting a movie and clicking "Show Recommendation," the system displays the top 5 recommended movies based on similarity.
- **Visual Presentation**: Recommendations are displayed with movie titles and posters in a visually appealing layout using Streamlit's column layout and Markdown support.

