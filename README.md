
# Book Recommendation System

## Overview

The Book Recommendation System is a web application built using **Streamlit**, which provides two main functionalities:
1. **Top 50 Books**: Displays the most popular books.
2. **Book Recommendation**: Suggests books similar to the one selected by the user.

The system is powered by pre-computed data and models to offer book recommendations based on similarity scores and popular trends.

## Features
- Displays the top 50 most popular books with images, titles, and authors.
- Provides personalized book recommendations based on a selected book.
- Offers a simple and clean user interface for book browsing.

## Tech Stack
- **Streamlit**: For building the web app interface.
- **Pandas**: For data manipulation and loading datasets.
- **NumPy**: For handling arrays and performing similarity calculations.
- **Pickle**: For loading pre-trained models and pre-computed data.
  
## Setup and Installation

To run the Book Recommendation System locally, follow these steps:

### 1. Clone the repository
```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Install dependencies
Make sure you have Python 3.x installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Required Files
Ensure you have the following pre-computed files:
- `popular.pkl`: Data on popular books.
- `books.pkl`: Contains details about the books (e.g., title, author, year).
- `pt.pkl`: A pivot table of book titles for recommendation.
- `similarity_scores.pkl`: The pre-computed similarity scores for recommending books.

### 4. Run the Streamlit app
After the dependencies are installed and the required files are available, you can run the app using:
```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser to use the application.

## Features Breakdown

### 1. **Top 50 Books**
In this tab, you can view a list of the most popular books. It displays:
- Book images
- Book titles
- Book authors

You can click on the "Show Top 50 Books" button to load the list.

### 2. **Book Recommendation**
In this tab, you can choose a book from the available list and get similar book recommendations. The recommended books are based on a similarity score calculated between books. Each recommendation includes:
- Book image
- Book title
- Book author
- Year of publication
- Publisher

## File Structure
- `app.py`: The main Python script that runs the Streamlit app.
- `popular.pkl`: Data file containing popular books.
- `books.pkl`: Data file containing details of the books.
- `pt.pkl`: Pivot table used for book recommendations.
- `similarity_scores.pkl`: Precomputed similarity scores between books.

## How It Works
- The app first loads data about books from pickle files.
- It displays the top 50 popular books or suggests recommendations based on the book selected by the user.
- Book recommendations are generated using similarity scores calculated between books using the pivot table.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [NumPy Documentation](https://numpy.org/doc/stable/)
