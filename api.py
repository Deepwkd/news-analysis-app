import os
from flask import Flask, request, jsonify
import requests
from utils import analyze_sentiment  

app = Flask(__name__)
API_KEY = os.getenv("NEWS_API_KEY")  #  Hugging Face Secret

# Function to fetch news articles from NewsAPI
def get_news(company_name):
    if not API_KEY:
        return {"error": "API Key missing"}

    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": f"Failed to fetch news. Status code: {response.status_code}"}
        return response.json().get("articles", [])[:10]
    except Exception as e:
        return {"error": str(e)}

# API endpoint: GET /news
@app.route('/news', methods=['GET'])
def news():
    company = request.args.get('company')
    if not company:
        return jsonify({"error": "Missing company parameter"}), 400

    articles = get_news(company)
    if isinstance(articles, dict) and "error" in articles:
        return jsonify(articles), 500

    processed_articles = []
    for article in articles:
        title = article.get("title", "No title available")
        summary = article.get("description", "No summary available")
        sentiment = analyze_sentiment(title)

        processed_articles.append({
            "title": title,
            "summary": summary,
            "sentiment": sentiment,
            "url": article.get("url", "#"),
        })

    return jsonify(processed_articles)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
