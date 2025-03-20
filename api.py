import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = os.getenv("NEWS_API_KEY")  # Reads from Hugging Face Secrets

def get_news(company_name):
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={API_KEY}"
    response = requests.get(url).json()
    return response.get("articles", [])

@app.route('/news', methods=['GET'])
def news():
    company = request.args.get('company')
    if not company:
        return jsonify({"error": "Missing company parameter"}), 400
    
    articles = get_news(company)
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
