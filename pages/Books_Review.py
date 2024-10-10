import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Books", books)

df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]
# df_book
# df_reviews_f

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_rating = df_book["rating"].iloc[0]
book_price = df_book["book price"].iloc[0]
book_year = df_book["year of publication"].iloc[0]
bool_url = df_book["url"].iloc[0]
book_author = df_book["author"].iloc[0]

st.title(book_title)
st.header(f"{book_author}")

col1, col2, col3 = st.columns(3)
col1.metric("Price",  f"$ {book_price}")
col2.metric("Rating", book_rating)
col3.metric("Year", book_year)

st.divider()

if not df_reviews_f.empty:
    st.subheader("Reviews")
else:
    st.subheader("No reviews")

for row in df_reviews_f.values:
    df_reviews_reviewers = row[2]
    df_reviews_review_desc = row[5]
    st.subheader(f"De {df_reviews_reviewers}")
    st.write(df_reviews_review_desc)
