import pandas as pd
import streamlit as st
import time
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from summa import keywords


st.set_page_config(page_title='News App',page_icon='👋')


# Initialize session state
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# Main function to calculate time spent in the app
def calculate_time_spent():
    end_time = time.time()
    time_spent = end_time - st.session_state.start_time
    return time_spent

# Streamlit web app - Main
def stopwatch():
    st.sidebar.title("Be the Master of Your Time! Track Your App Sessions")
    #st.sidebar.markdown("---")
    
    # Calculate time spent when "Calculate" button is clicked
    if st.sidebar.button("Calculate"):
        time_spent = calculate_time_spent()
        st.sidebar.write(f"Time Spent in the App: {int(time_spent)} seconds")

stopwatch()
    

# Step 1: Load news data from CSV file
news_data = pd.read_csv('news_data.csv')

# Step 2: Load comic data from CSV file
comic_data = pd.read_csv('comic_data.csv')

# Step 3: Extract keywords from news article using TextRank algorithm
def extract_keywords(text):
    return keywords.keywords(text).split('\n')


# Step 4: Calculate TF-IDF scores for comic content and news articles
def calculate_similarity_scores():
    vectorizer = TfidfVectorizer()
    comic_tfidf = vectorizer.fit_transform(comic_data['content'])
    news_tfidf = vectorizer.transform(news_data['text'])
    similarity_scores = cosine_similarity(news_tfidf, comic_tfidf)
    return similarity_scores


# Step 5: Streamlit web app
st.title("Crime News App 😱")
st.subheader("Latest Titles 🩸")


# Display news articles
def getnews():
    for index, row in news_data.iterrows():
        st.write(f"## {row['title']}")
        st.write(row['text'])
        if st.button(f'Read more #{index}', key=f"read_more_{index}"):
            article_text = row['text']
            keywords = extract_keywords(article_text)
            similarity_scores = calculate_similarity_scores()
            relevant_comics = []
            for idx, score in enumerate(similarity_scores[index]):
                if score > 0:
                    relevant_comics.append(comic_data['content'][idx])
            if relevant_comics:
                st.subheader("Recommended Content")
                for comic_content in relevant_comics[:3]:  # Display the first three comics
                    st.write(comic_content)
            else:
                st.write("No comic content found for this article.")
        st.write('---')

getnews()













      