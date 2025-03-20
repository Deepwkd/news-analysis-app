
import streamlit as st
import requests
from textblob import TextBlob
from gtts import gTTS
import os
import json
from deep_translator import GoogleTranslator 

# Reading API Key from Hugging Face Secrets
API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    st.error("Error: NEWS_API_KEY not found. Set it in Hugging Face Secrets.")

# to fetch news articles using NewsAPI
def get_news_articles(company_name):
    if not API_KEY:
        st.error("Error: NEWS_API_KEY not found. Set it in the .env file or Hugging Face Secrets.")
        return []
    
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if "articles" not in data or not data["articles"]:
        return []
    
    news_list = [(article["title"], article["url"], article.get("description", "No summary available")) for article in data["articles"][:10]]
    return news_list

# Sentiment analysis function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity
    
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

# Text-to-Speech conversion ( translation to Hindi using deep-translator)
def text_to_speech(text):
    try:
        # Translating the text to Hindi using deep-translator
        translated_text = GoogleTranslator(source='en', target='hi').translate(text)
        
        # Generate Hindi speech
        tts = gTTS(text=translated_text, lang='hi')
        tts.save("summary.mp3")
        return "summary.mp3"
    
    except Exception as e:
        st.error(f"Error in text-to-speech: {e}")
        return None

# Streamlit UI
st.title("🔍 News Sentiment Analysis")
company_name = st.text_input("Enter Company Name:")

if st.button("Fetch News & Analyze"):
    articles = get_news_articles(company_name)
    
    if not articles:
        st.write("⚠️ No articles found. Try another company name.")
    else:
        sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
        summarized_text = ""
        
        st.subheader("📰 News Articles")
        for title, link, summary in articles:
            sentiment = analyze_sentiment(title)
            sentiment_counts[sentiment] += 1
            summarized_text += title + ". "
            
            st.write(f"**Title:** {title}")
            st.write(f"**Summary:** {summary}")
            st.write(f"**Sentiment:** {sentiment}")
            st.write(f"[🔗 Read More]({link})")
            st.write("---")
        
        # Comparative Analysis
        st.subheader("📊 Comparative Sentiment Analysis")
        st.json(sentiment_counts)
        
        # Text-to-Speech
        st.subheader("🗣️ Hindi Speech Output")
        speech_file = text_to_speech(summarized_text)
        if speech_file:
            st.audio(speech_file, format='audio/mp3')
