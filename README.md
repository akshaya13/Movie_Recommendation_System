# Movie Recommendation System - Content-Based Recommendation System
### Overview

This project implements a content-based movie recommendation system utilizing the TMDB 5000 dataset from Kaggle. The system analyzes various movie attributes to generate personalized recommendations based on user input.

### Dataset
Source: TMDB 5000 Dataset (https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

Version 1: Stemming + Bag of Words + Similarity Search
Version 2: Lemmatization + TFIDF + Similarity Search

### Steps
* Data Preprocessing: Clean and prepare the dataset for analysis.
* Exploratory Data Analysis (EDA): Analyze the dataset to understand its structure and key features.
* Feature Engineering: Extract meaningful features from the dataset to enhance recommendation accuracy.
* Tag Creation: Generate tags based on multiple columns including Genre, Overview, Keywords, Cast, and Crew.
* Text Processing: Apply stemming and lemmatization techniques, and remove stop words to refine the tags for better similarity matching.
* Cosine similarity is applied to find the similar movies
