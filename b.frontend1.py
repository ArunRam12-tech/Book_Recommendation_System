import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import os

# Load models
books = pickle.load(open('books.pkl', 'rb'))
kmeans = pickle.load(open('kmeans.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

# Ensure clean title column exists
if 'title_clean' not in books.columns:
    books['title_clean'] = books['title'].str.lower().str.strip()


# Recommendation function
def get_recommendations(title, books, top_n=5):
    title_clean = title.strip().lower()
    if title_clean not in books['title_clean'].values:
        return ["❌ Book not found in dataset."]

    cluster_id = books.loc[books['title_clean'] == title_clean, 'cluster'].values[0]
    similar_books = books[books['cluster'] == cluster_id]
    similar_books = similar_books[similar_books['title_clean'] != title_clean]

    return similar_books[['title', 'authors', 'categories', 'image_path']].head(top_n)


# Streamlit UI
st.set_page_config(page_title="Book Recommender", layout="wide")
st.title("📚 Book Recommender System (KMeans)")

book_list = sorted(books['title'].unique())
selected_book = st.selectbox("Select a book:", book_list)
top_n = st.slider("Number of recommendations:", 1, 10, 5)

if st.button("Recommend"):
    recommendations = get_recommendations(selected_book, books, top_n)

    if isinstance(recommendations, list):
        st.error(recommendations[0])
    else:
        st.success(f"📖 Recommendations for **{selected_book}**:")

        for idx, row in recommendations.iterrows():
            cols = st.columns([1, 3])

            # Load and display local image if available
            with cols[0]:
                if pd.notna(row['image_path']) and os.path.exists(row['image_path']):
                    image = Image.open(row['image_path'])
                    st.image(image, width=120)

            # Display book info
            with cols[1]:
                st.markdown(f"**{row['title']}**")
                st.markdown(f"*by {row['authors']}*")
                st.markdown(f"Category: {row['categories']}")

            st.markdown("---")
