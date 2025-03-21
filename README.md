# 📰 News Sentiment Analysis (with Hindi Audio)

This project extracts and analyzes recent news articles about a company, performs sentiment analysis, and generates a Hindi audio summary using TTS. The app is fully deployable on Hugging Face Spaces and satisfies API-based architecture requirements.

---

## 🚀 Features

- ✅ Fetches latest news articles using NewsAPI
- ✅ Performs sentiment analysis (Positive / Negative / Neutral)
- ✅ Generates comparative sentiment analysis
- ✅ Converts sentiment summary to Hindi speech using gTTS
- ✅ Streamlit UI integrated with Flask API (inside one file using threading)
- ✅ Ready for deployment on Hugging Face Spaces

---

## 🔧 1️⃣ Setup Instructions (Local)

### 🔹 Clone the Repository

```bash
git clone https://github.com/your-username/news-sentiment-analysis
cd news-sentiment-analysis

🔹 Set Up API Key
Get a free NewsAPI key from NewsAPI.org.
Create a .env file with your API key:


2️⃣ Code Structure
File	Purpose
app.py	Combined Flask backend + Streamlit frontend
utils.py	Sentiment analysis logic using TextBlob
api.py	Optional modular Flask API (for testing/showing structure)
requirements.txt	Python dependencies for the app

3️⃣ Deploy to Hugging Face Spaces
🔹 Create a New Space
Visit: https://huggingface.co/spaces
Click Create New Space
Choose "Python" as the space template

🔹 Upload Files
app.py ✅
utils.py ✅
requirements.txt ✅
(Optional) api.py for modular API structure

🔹 Add Secret
Go to Settings → Secrets in your Hugging Face Space
Add:
Name: NEWS_API_KEY
Value: your actual NewsAPI key

4️⃣ Project Setup
Installation
Python version: 3.8+
Install dependencies using: pip install -r requirements.txt
Run the app locally with: streamlit run app.py


5️⃣ Model Details
🧠 Sentiment Analysis
Library: TextBlob
Method: Polarity scoring of article titles
Output: Positive / Negative / Neutral

📢 Text-to-Speech
Library: gTTS (Google Text-to-Speech)
Language: Hindi (lang='hi')
Output: .mp3 audio summary of headlines and sentiment

🗣️ Summarization
Custom summarization of top 5 titles + sentiment distribution
Translated into Hindi using deep-translator (Google Translate backend)


6️⃣ API Development
Backend is built using Flask inside app.py
A threaded Flask server runs on port 5000
API Endpoint:
GET /news?company=Tesla
Returns list of article titles, summaries, sentiment, and links

7️⃣ API Usage (Third-party)
API / Service	    Purpose	                       Integration
NewsAPI.org	      Fetch news articles	           Used in get_news() function
gTTS	            Convert text to Hindi audio	   Used in frontend TTS
deep-translator	  Translate English summary      Before TTS
TextBlob	        Perform sentiment analysis	   Based on title polarity

8️⃣ Assumptions & Limitations

✅ Assumptions
The title of an article represents the sentiment of the full article
Top 10 articles are enough to reflect sentiment trends
Google Translate provides good enough Hindi accuracy for TTS

⚠️ Limitations
TTS audio is limited to ~60 seconds
NewsAPI results may include duplicates or outdated links
Sentiment analysis is simple and not context-aware
Requires stable internet connection for API calls and TTS
