
import os
from flask import Flask, request, jsonify
import requests
from utils import analyze_sentiment, translate_text  # Importing utility functions

app = Flask(__name__)
API_KEY = os.getenv("NEWS_API_KEY")  # Reads from Hugging Face Secrets

# Function to fetch news articles
def get_news(company_name):
    """Fetch news articles from NewsAPI for a given company."""
    if not API_KEY:
        return {"error": "API Key missing"}, 400

    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch news"}, response.status_code

    data = response.json()
    articles = data.get("articles", [])
    
    result = []
    for article in articles[:10]:  # Limiting to 10 articles
        title = article.get("title", "No title available")
        description = article.get("description", "No description available")
        url = article.get("url", "")

        sentiment = analyze_sentiment(title)  # Sentiment Analysis
        translated_summary = translate_text(description)  # Translate summary to Hindi

        result.append({
            "title": title,
            "summary": description,
            "sentiment": sentiment,
            "translated_summary": translated_summary,
            "url": url
        })
    
    return result

# API Route to Fetch News and Perform Sentiment Analysis
@app.route('/news', methods=['GET'])
def news():
    """API endpoint to fetch news and analyze sentiment."""
    company = request.args.get('company')
    if not company:
        return jsonify({"error": "Missing company parameter"}), 400
    
    articles = get_news(company)
    return jsonify(articles)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
