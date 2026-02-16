The Book Recommender System is a machine learning–based application designed to suggest books that are similar to a user’s selected title. The system uses a dataset containing information such as title, subtitle, authors, categories, and descriptions. These textual features are combined into a single representation to capture the overall theme and content of each book. The combined text is then converted into numerical form using TF-IDF vectorization, which assigns importance to meaningful and distinctive words across the dataset.

After vectorization, the system applies the KMeans clustering algorithm to group books with similar content into the same clusters. Each book is assigned a cluster label that represents its content-based category. When a user selects a book, the system identifies its cluster and retrieves other books from the same group, recommending the top similar titles. The application is built with an interactive Streamlit interface, allowing users to easily select a book, adjust the number of recommendations, and view results along with authors, categories, and cover images. This project demonstrates practical skills in natural language processing, machine learning, data preprocessing, clustering, and web application development.

Skills Used

Python

Pandas

Scikit-learn

TF-IDF (Text Vectorization)

KMeans Clustering

Machine Learning

Data Preprocessing

Streamlit

Pickle (Model Serialization)

PIL (Image Handling)
