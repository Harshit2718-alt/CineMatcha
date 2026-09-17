# 🎬 CineMatcha

This is a simple **AI/ML-based Movie Recommendation System** built using
Python.\
The project recommends movies that are similar to a movie selected by
the user.

The system uses **TF-IDF Vectorization** and **Cosine Similarity** to
compare movie genres and descriptions and generate recommendations.

------------------------------------------------------------------------

## ✨ Features

-   🎬 Select a movie from the available movie list
-   🤖 Uses machine learning techniques for recommendations
-   📝 Analyzes movie genre and description
-   📊 Converts text into numerical features using **TF-IDF**
-   🔍 Finds similar movies using **Cosine Similarity**
-   ⭐ Shows the top 5 recommended movies
-   📈 Displays a similarity percentage for each recommendation
-   💻 Simple Python implementation that can run directly in Google
    Colab

------------------------------------------------------------------------

## 🧠 How the System Works

### 1. Movie Data

The project contains movie information such as:

-   Movie title
-   Genre
-   Description

The genre and description are combined to create the movie's feature
information.

### 2. TF-IDF Vectorization

The movie features are converted from text into numerical values using:

**TF-IDF (Term Frequency--Inverse Document Frequency)**

This allows the computer to understand which words are important when
comparing movies.

### 3. Cosine Similarity

The system compares the numerical movie vectors using **Cosine
Similarity**.

A higher similarity value means that two movies have more similar
features.

### 4. Recommendation

After the user enters a movie name:

``` text
User selects a movie
        ↓
Movie features are selected
        ↓
TF-IDF converts text into vectors
        ↓
Cosine Similarity compares movies
        ↓
Movies are sorted by similarity
        ↓
Top 5 movies are recommended
```

------------------------------------------------------------------------

## 🤖 AI / ML Used

The main machine learning concepts used in this project are:

-   **Content-Based Filtering**
-   **TF-IDF Vectorization**
-   **Cosine Similarity**
-   **Natural Language Processing (NLP)**

The system follows a **content-based recommendation approach**, because
recommendations are generated from the characteristics of the selected
movie.

------------------------------------------------------------------------

## 📂 Project Structure

``` text
Movie-Recommendation-System/
│
├── movie_recommendation.py
└── README.md
```

For the Google Colab version, the complete Python code can simply be
placed inside a notebook cell.

------------------------------------------------------------------------

## ▶️ How to Run

### Google Colab

1.  Open Google Colab.
2.  Create a new notebook.
3.  Run the required libraries:

``` python
!pip install pandas scikit-learn -q
```

4.  Paste the Movie Recommendation System code into the next cell.
5.  Run the cell.
6.  Enter a movie name when prompted.

Example:

``` text
Enter a movie you like: Inception
```

------------------------------------------------------------------------

## 📊 Sample Output

``` text
🎬 MOVIE RECOMMENDATION SYSTEM
========================================

Available Movies:
• Inception
• Interstellar
• The Dark Knight
• The Matrix
• Iron Man
• Avengers Endgame
• Avatar
• Jurassic Park
• Titanic
• The Shawshank Redemption

Type 'exit' to close the program.

Enter a movie you like: Inception

🎬 Recommended Movies
===================================
1. The Matrix (similarity %)
2. Interstellar (similarity %)
3. Avatar (similarity %)
4. Iron Man (similarity %)
5. Jurassic Park (similarity %)
```

> The exact similarity percentages can change depending on the movie
> data and feature descriptions.

------------------------------------------------------------------------

## 🛠️ Technologies Used

  Technology          Purpose
  ------------------- ---------------------------------
  Python              Main programming language
  Pandas              Managing movie data
  Scikit-learn        Machine learning calculations
  TF-IDF              Text feature extraction
  Cosine Similarity   Movie similarity calculation
  Google Colab        Running and testing the project

------------------------------------------------------------------------

## 📌 Example

If the user enters:

``` text
Inception
```

the system looks at the features of **Inception** and compares them with
the other movies.

Because movies such as *The Matrix* and *Interstellar* contain related
**Sci-Fi / Thriller / Adventure** features, they can receive higher
similarity scores.

------------------------------------------------------------------------

## 🚀 Future Improvements

The project can be expanded by adding:

-   👤 User accounts and movie ratings
-   ⭐ Personalized recommendations based on rating history
-   👥 Collaborative Filtering
-   🎞️ A larger real-world movie dataset
-   🖼️ Movie posters and details
-   🔎 Movie search
-   🌐 Web interface using Flask or Streamlit
-   🎯 Hybrid recommendation system combining content-based and
    collaborative filtering

------------------------------------------------------------------------

## 🎓 Project Objective

The main objective of this project is to demonstrate how **AI/ML
techniques can be used to build a recommendation system**.

Instead of manually selecting movies, the system analyzes movie
information and automatically finds movies with similar characteristics.

------------------------------------------------------------------------

## 👨‍💻 Conclusion

The Movie Recommendation System demonstrates a practical application of
**machine learning and NLP**.

By using **TF-IDF** and **Cosine Similarity**, the system converts movie
descriptions into machine-readable features and recommends movies based
on their similarity.

Code:
<br>
<br>
<img width="506" height="902" alt="image" src="https://github.com/user-attachments/assets/a71c4244-4a97-4656-b284-4238258bc582" />
<br>
<br>
<img width="411" height="905" alt="image" src="https://github.com/user-attachments/assets/734d06c7-af9e-4872-b99c-9d623df782d3" />
<br>
<br>
<img width="641" height="537" alt="image" src="https://github.com/user-attachments/assets/9627de78-3cd0-4681-80cf-479ba05e46a3" />

