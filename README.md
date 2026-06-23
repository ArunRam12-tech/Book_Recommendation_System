# Book Recommender System 📚

## Overview

The Book Recommender System is a Machine Learning-based application that recommends books similar to a user's selected title. The system analyzes book information such as title, subtitle, authors, categories, and descriptions to identify content-based similarities and provide personalized recommendations.

The application uses Natural Language Processing (NLP) techniques and Machine Learning algorithms to group books with similar themes and suggest relevant titles. An interactive Streamlit interface allows users to easily explore recommendations along with book details and cover images.

---

## Features

* Book recommendation based on content similarity
* Interactive Streamlit web interface
* Search and select books from the dataset
* Adjustable number of recommendations
* Display of book title, author, category, and cover image
* Fast and efficient recommendation generation
* Content-based recommendation approach

---

## Technologies Used

### Programming Language

* Python

### Machine Learning & NLP

* Scikit-learn
* TF-IDF Vectorization
* KMeans Clustering

### Libraries

* Pandas
* NumPy
* Pickle
* PIL (Python Imaging Library)

### Web Development

* Streamlit

---

## Dataset Features

The system utilizes the following book attributes:

* Title
* Subtitle
* Authors
* Categories
* Description

These features are combined into a single text representation to capture the overall content and theme of each book.

---

## Methodology

### 1. Data Preprocessing

* Handling missing values
* Cleaning textual data
* Combining relevant text features
* Feature engineering

### 2. Text Vectorization

TF-IDF (Term Frequency-Inverse Document Frequency) is used to convert textual information into numerical vectors.

Benefits:

* Identifies important words
* Reduces influence of common terms
* Captures meaningful book content

### 3. Clustering

KMeans Clustering is applied to group books with similar content.

* Similar books are assigned to the same cluster
* Each cluster represents a content-based category
* Recommendations are generated from the same cluster

### 4. Recommendation Generation

When a user selects a book:

1. Identify the book's cluster
2. Retrieve books from the same cluster
3. Rank similar books
4. Display top recommendations

---

## System Workflow

```text
Book Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Combination
      │
      ▼
TF-IDF Vectorization
      │
      ▼
KMeans Clustering
      │
      ▼
Cluster Assignment
      │
      ▼
Book Recommendation
```

---

## Project Structure

```text
Book-Recommender-System/
├── app.py
├── books.csv
├── model.pkl
├── tfidf.pkl
├── requirements.txt
├── images/
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Book-Recommender-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Skills Demonstrated

* Python Programming
* Machine Learning
* Natural Language Processing (NLP)
* Data Preprocessing
* Feature Engineering
* TF-IDF Vectorization
* KMeans Clustering
* Model Serialization using Pickle
* Streamlit Web Application Development

---

## Future Enhancements

* Collaborative Filtering
* Hybrid Recommendation System
* User Login and Profiles
* Personalized Recommendations
* Book Rating Prediction
* Integration with Online Book APIs

---

## Author

**Arun H**

B.E. Computer Science Engineering
ACS College of Engineering

### Skills Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorization
* KMeans Clustering
* Machine Learning
* Data Preprocessing
* Streamlit
* Pickle
* PIL

---

⭐ If you found this project useful, consider giving it a star.
