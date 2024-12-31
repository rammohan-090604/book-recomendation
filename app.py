# import streamlit as st
# import pickle
# import pandas as pd
# import numpy as np

# # Set the page configuration for the app
# st.set_page_config(page_title="Book Recommendation System", layout="wide")

# # Page Title and Welcome Text
# st.title("Book Recommendation System")
# st.write("Welcome to the Book Recommendation System. Please explore the most popular books or get personalized recommendations.")

# # Importing the models (example data)
# popular = pickle.load(open("popular.pkl", "rb"))  # Precomputed popular books
# books = pickle.load(open("books.pkl", "rb"))
# pt = pickle.load(open("pt.pkl", "rb"))
# similarity_scores = pickle.load(open("similarity_scores.pkl", "rb"))

# # Sidebar title and button for popular books
# st.sidebar.title("Top 50 Books")

# # Show a loading spinner when the button is pressed
# if st.sidebar.button("Show Top 50 Books"):
#     with st.spinner('Loading popular books...'):
#         st.write("### Most Popular Books")
        
#         # Define the number of books per row
#         col_per_row = 5
#         num_books = len(popular)

#         # Create rows and columns for displaying popular books
#         for i in range(0, num_books, col_per_row):
#             cols = st.columns(col_per_row)  # Create a row with 5 columns
#             for col, book_idx in zip(cols, range(i, min(i + col_per_row, num_books))):
#                 book = popular.iloc[book_idx]
#                 # Display book image, title, and author
#                 with col:
#                     st.image(book["Image-URL-M"], width=100)  # Display image
#                     st.markdown(f"**{book['Book-Title']}**")  # Display title
#                     st.markdown(f"*{book['Book-Author']}*")  # Display author

# # Recommending the books based on Cosine similarity

# def recomendation(book_name):
#     index = np.where(pt.index == book_name)[0][0]
#     similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
    
#     recommended_books = []
#     for i, score in similar_items:
#         recommended_books.append(
#             {
#                 'title': pt.index[i],
#                 'author': books[books['Book-Title'] == pt.index[i]]['Book-Author'].values[0] if len(books[books['Book-Title'] == pt.index[i]]['Book-Author'].values) > 0 else "N/A",
#                 'image': books[books['Book-Title'] == pt.index[i]]['Image-URL-M'].values[0] if len(books[books['Book-Title'] == pt.index[i]]['Image-URL-M'].values) > 0 else "N/A",
#                 'year': books[books['Book-Title'] == pt.index[i]]['Year-Of-Publication'].values[0] if len(books[books['Book-Title'] == pt.index[i]]['Year-Of-Publication'].values) > 0 else "N/A",
#                 'publisher': books[books['Book-Title'] == pt.index[i]]['Publisher'].values[0] if len(books[books['Book-Title'] == pt.index[i]]['Publisher'].values) > 0 else "N/A",
#             }
#         )
    
#     return recommended_books

# books_list = pt.index.values
# st.sidebar.title("Similar Book Recommendations")
# selected_book = st.selectbox("Select a book", books_list)

# if st.sidebar.button("SHOW"):
#     book_recommendations = recomendation(selected_book)
    
#     # Create columns to display the recommendations
#     cols = st.columns(5)
    
#     # Loop through the recommendations and display them
#     for col, book in zip(cols, book_recommendations):
#         with col:
#             st.image(book['image'], width=100)  # Display image
#             st.markdown(f"**{book['title']}**")  # Display title
#             st.markdown(f"*{book['author']}*")  # Display author

import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Set the page configuration for the app
st.set_page_config(page_title="Book Recommendation System", layout="wide")

# Page Title and Welcome Text
st.title("Book Recommendation System")
st.write("Welcome to the Book Recommendation System. Please explore the most popular books or get personalized recommendations.")

# Importing the models (example data)
popular = pickle.load(open("popular.pkl", "rb"))  # Precomputed popular books
books = pickle.load(open("books.pkl", "rb"))
pt = pickle.load(open("pt.pkl", "rb"))
similarity_scores = pickle.load(open("similarity_scores.pkl", "rb"))

# Sidebar for selecting tabs
tabs = st.sidebar.radio("Select a tab", ("Top 50 Books", "Book Recommendation"))

# Tab 1: Display Top 50 Books
if tabs == "Top 50 Books":
    st.sidebar.title("Top 50 Books")
    
    if st.sidebar.button("Show Top 50 Books"):
        with st.spinner('Loading popular books...'):
            st.write("### Most Popular Books")
            
            # Define the number of books per row
            col_per_row = 5
            num_books = len(popular)

            # Create rows and columns for displaying popular books
            for i in range(0, num_books, col_per_row):
                cols = st.columns(col_per_row)  # Create a row with 5 columns
                for col, book_idx in zip(cols, range(i, min(i + col_per_row, num_books))):
                    book = popular.iloc[book_idx]
                    # Display book image, title, and author
                    with col:
                        st.image(book["Image-URL-M"], width=100)  # Display image
                        st.markdown(f"**{book['Book-Title']}**")  # Display title
                        st.markdown(f"*{book['Book-Author']}*")  # Display author

# Tab 2: Book Recommendation
elif tabs == "Book Recommendation":
    st.sidebar.title("Similar Book Recommendations")

    def recomendation(book_name):
        index = np.where(pt.index == book_name)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
        
        recommended_books = []
        for i, score in similar_items:
            recommended_books.append(
                {
                    'title': pt.index[i],
                    'author': books[books['Book-Title'] == pt.index[i]]['Book-Author'].values[0] if len(books[books['Book-Title'] == pt.index[i]]['Book-Author'].values) > 0 else "N/A",
                    'image': books[books['Book-Title'] == pt.index[i]]['Image-URL-M'].values[0] if len(books[books['Book-Title'] == pt.index[i]]['Image-URL-M'].values) > 0 else "N/A",
                    'year': books[books['Book-Title'] == pt.index[i]]['Year-Of-Publication'].values[0] if len(books[books['Book-Title'] == pt.index[i]]['Year-Of-Publication'].values) > 0 else "N/A",
                    'publisher': books[books['Book-Title'] == pt.index[i]]['Publisher'].values[0] if len(books[books['Book-Title'] == pt.index[i]]['Publisher'].values) > 0 else "N/A",
                }
            )
        
        return recommended_books

    books_list = pt.index.values
    selected_book = st.selectbox("Select a book", books_list)

    if st.button("Get Recommendations"):
        book_recommendations = recomendation(selected_book)
        
        # Create columns to display the recommendations
        cols = st.columns(5)
        
        # Loop through the recommendations and display them
        for col, book in zip(cols, book_recommendations):
            with col:
                st.image(book['image'], width=100)  # Display image
                st.markdown(f"**{book['title']}**")  # Display title
                st.markdown(f"*{book['author']}*")  # Display author
