!pip install pandas scikit-learn -q

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Movie data
movies = pd.DataFrame({
    "title": [
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "The Matrix",
        "Iron Man",
        "Avengers Endgame",
        "Avatar",
        "Jurassic Park",
        "Titanic",
        "The Shawshank Redemption"
    ],

    "genre": [
        "Action Sci-Fi Thriller",
        "Adventure Drama Sci-Fi",
        "Action Crime Drama",
        "Action Sci-Fi Thriller",
        "Action Sci-Fi",
        "Action Adventure Sci-Fi",
        "Action Adventure Sci-Fi",
        "Adventure Sci-Fi Thriller",
        "Drama Romance",
        "Drama Crime"
    ],

    "description": [
        "A thief enters dreams to steal important information.",
        "Astronauts travel through space searching for a new home.",
        "Batman fights crime and a dangerous enemy in Gotham.",
        "A hacker discovers that the world is a computer simulation.",
        "A billionaire creates a powerful suit and becomes a superhero.",
        "Superheroes come together to fight a powerful enemy.",
        "A soldier travels to another planet and meets an alien civilization.",
        "Scientists create dinosaurs for a special theme park.",
        "Two people fall in love despite their different backgrounds.",
        "A prisoner makes friends and dreams about freedom."
    ]
})


# Combine genre and description
movies["features"] = (
    movies["genre"] + " " + movies["description"]
)


# Convert text into numerical values
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(movies["features"])


# Calculate similarity between movies
similarity_matrix = cosine_similarity(tfidf_matrix)


def recommend_movies(movie_name):

    movie_name = movie_name.strip().lower()

    # Find the selected movie
    matches = movies[
        movies["title"].str.lower() == movie_name
    ]

    if matches.empty:
        print("\n❌ Movie not found.")
        print("Please select a movie from the list.")
        return

    movie_index = matches.index[0]

    # Get similarity scores
    scores = list(
        enumerate(similarity_matrix[movie_index])
    )

    # Highest similarity first
    scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\n🎬 Recommended Movies")
    print("=" * 35)

    count = 0

    for index, score in scores:

        # Don't recommend the movie itself
        if index == movie_index:
            continue

        print(
            f"{count + 1}. "
            f"{movies.iloc[index]['title']} "
            f"({score * 100:.1f}% similar)"
        )

        count += 1

        if count == 5:
            break


# Display available movies
print("🎬 MOVIE RECOMMENDATION SYSTEM")
print("=" * 40)

print("\nAvailable Movies:")

for movie in movies["title"]:
    print("•", movie)


# Ask the user for a movie
movie = input(
    "\nEnter a movie you like: "
)

recommend_movies(movie)