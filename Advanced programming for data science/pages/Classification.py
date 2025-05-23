
#Code for the LLM Part: 
import streamlit as st
import random
import matplotlib.pyplot as plt
from movie_data_v2 import MovieData
import ollama
from ollama import chat, ChatResponse

# Initialize MovieData instance
url = "http://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz"
test_instance = MovieData(url=url)

# Set page title
st.title("Random Movie Information")

# Filter movies with existing summaries and genres
valid_movies = test_instance.movie_df[
    #(test_instance.movie_df["wikipedia_movie_id"].isin(test_instance.plot_summaries["wikipedia_movie_id"])) &
    (test_instance.movie_df["genres"].notna())
]

# Shuffle button
if st.button("Shuffle"):
    # Ensure there are valid movies to choose from
    if valid_movies.empty:
        st.error("No movies with summaries and genres available.")
    else:
        # Select a random movie from the filtered list
        random_index = random.randint(0, len(valid_movies) - 1)
        movie = valid_movies.iloc[random_index]
        movie_id = movie["wikipedia_movie_id"]
        
        # Get the movie title and summary
        movie_title = movie["title"]
        plot_summary_row = test_instance.plot_summaries[test_instance.plot_summaries["wikipedia_movie_id"] == movie_id]
        
        if not plot_summary_row.empty:
            movie_summary = plot_summary_row["plot_summary"].values[0]
        else:
            movie_summary = "Summary not available."
        
        # Get the movie genres
        movie_genres = eval(movie["genres"]).values()
        
        # Display the information in text boxes
        st.markdown(f"### {movie_title}\n\n{movie_summary}")
        st.text_area("Genres", ", ".join(movie_genres))
        # Use local LLM to classify the genre
        response: ChatResponse = chat(model='mistral', messages=[
            {
                'role': 'user',
                'content': f"Classify the following movie summary into genres: {movie_summary}. The genres should be one word, for example don't say Political Thriller, only Thriller. Only list the genres, separated by commas. Do not include any additional information or brackets.",
            },
        ])
        
        # Extract and display the genre classification
        llm_genres = response.message.content.strip()
        st.text_area("Genre by LLM", llm_genres)
        
        # Normalize and compare genres
        identified_genres = set([genre.strip().lower() for genre in llm_genres.split(",")])
        database_genres = set([genre.strip().lower() for genre in movie_genres])
        
        matching_genres = identified_genres.intersection(database_genres)
        
        if matching_genres:
            st.markdown("### Successfully Detected Genres")
            st.markdown(", ".join(matching_genres))
        
        if identified_genres.issubset(database_genres):
            st.success("It's a perfect match. The LLM works!!!")
        else:
            st.warning("It's not you it's me. The LLM made some bad decisions.")
        
        # Visualization of the score
        genre_counts = {
            "Database Genres": len(database_genres),
            "LLM Genres": len(identified_genres),
            "Matching Genres": len(matching_genres)
        }
        
        fig, ax = plt.subplots()
        ax.bar(genre_counts.keys(), genre_counts.values(), color=["purple", "black", "lightgreen"])
        ax.set_ylabel("Count")
        ax.set_title("Genre Detection Score")
        st.pyplot(fig)
