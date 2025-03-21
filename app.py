import streamlit as st
import requests
from gtts import gTTS
from deep_translator import GoogleTranslator
import threading
import os
from flask import Flask, request, jsonify
from utils import analyze_sentiment

# ------------------- Start Flask Backend (like api.py) ---------------------
flask_app = Flask(__name__)
API_KEY = os.getenv("NEWS_API_KEY")

@flask_app.route('/news', methods=['GET'])
def news():
    company = request.args.get('company')
    if not company:
        return jsonify({"error": "Missing company parameter"}), 400

    url = f"https://newsapi.org/v2/everything?q={company}&apiKey={API_KEY}"
    try:
        response = requests.get(url)
        articles = response.json().get("articles", [])[:10]
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    processed = []
    for article in articles:
        title = article.get("title", "No title")
        summary = article.get("description", "No summary")
        sentiment = analyze_sentiment(title)
        processed.append({
            "title": title,
            "summary": summary,
            "sentiment": sentiment,
            "url": article.get("url", "#")
        })
    return jsonify(processed)

def run_flask():
    flask_app.run(host="0.0.0.0", port=5000)

# Start Flask server in a thread
threading.Thread(target=run_flask, daemon=True).start()

# ------------------- Streamlit Frontend ---------------------
st.title("🔍 News Sentiment Analysis")
company_name = st.text_input("Enter Company Name:")

def get_news_articles(company):
    try:
        url = f"http://localhost:5000/news?company={company}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to connect to backend API: {e}")
        return []

def generate_hindi_audio(titles, positive, negative, neutral, company):
    try:
        title_summary = "Top headlines include: " + "; ".join(titles[:5]) + "."
        sentiment_summary = (
            f"There are {positive} positive, {negative} negative, and {neutral} neutral articles "
            f"about {company}. This shows a mixed sentiment in the media coverage."
        )
        full_summary = f"{title_summary} {sentiment_summary}"
        translated = GoogleTranslator(source='en', target='hi').translate(full_summary)
        tts = gTTS(text=translated, lang='hi')
        tts.save("summary.mp3")
        return "summary.mp3"
    except Exception as e:
        st.error(f"Text-to-speech error: {e}")
        return None

if st.button("Fetch News & Analyze"):
    articles = get_news_articles(company_name)
    if not articles:
        st.warning("⚠️ No articles found. Try another company.")
    else:
        sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
        titles = []

        st.markdown("#### 📄 Structured News Report")
        for article in articles:
            title = article["title"]
            summary = article["summary"]
            sentiment = article["sentiment"]
            url = article["url"]

            titles.append(title)
            sentiment_counts[sentiment] += 1

            st.markdown(f"""
            <div style='font-size: 14px; line-height: 1.6;'>
            <b>📰 Title:</b> {title}<br>
            <b>📝 Summary:</b> {summary}<br>
            <b>📊 Sentiment:</b> {sentiment}<br>
            <b>🔗 <a href="{url}" target="_blank">Read Full Article</a></b>
            </div>
            <hr>
            """, unsafe_allow_html=True)

        st.markdown("#### 📊 Comparative Sentiment Analysis")
        st.json({"Sentiment Distribution": sentiment_counts})

        st.markdown("#### 🗣️ Hindi Speech Output")
        audio = generate_hindi_audio(
            titles,
            sentiment_counts["Positive"],
            sentiment_counts["Negative"],
            sentiment_counts["Neutral"],
            company_name
        )
        if audio:
            st.audio(audio, format="audio/mp3")
