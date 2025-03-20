# News Sentiment Analysis

This project extracts, analyzes, and summarizes news articles about companies, providing sentiment analysis and Hindi text-to-speech conversion.

## Features
- Fetches news articles using NewsAPI
- Performs sentiment analysis (Positive, Neutral, Negative)
- Converts summaries to Hindi speech
- Provides a Streamlit-based UI
- Includes a Flask API for backend communication
- Deployable on Hugging Face Spaces

---

## **1️⃣ Setup Instructions**

### **🔹 Clone the Repository**
```bash
git clone https://github.com/your-username/news-sentiment-analysis
cd news-sentiment-analysis
```

### **🔹 Install Dependencies**
```bash
pip install -r requirements.txt
```

### **🔹 Set Up API Key**
1. Get a **free NewsAPI key** from [NewsAPI.org](https://newsapi.org/).
2. Add the API key to Hugging Face Secrets (if deploying) or create a `.env` file:
```bash
echo "API_KEY=your_api_key" > .env
```

## **3️⃣ Code Files**

 **📌 `app.py` (Main Streamlit App)**

 **📌 `api.py` (API Backend)**

 **📌 `utils.py` (Utility Functions)**

 **📌 `requirements.txt` (Dependencies)**
```

## 4️⃣ Run the Project Locally

### 🔹 Start the Streamlit App

### 🔹 Start the API Backend

## 5️⃣ Deploy on Hugging Face

### 🔹 Clone the Hugging Face Space


### 🔹 Add API Key in Hugging Face Secrets
1. Go to **Settings** → **Secrets**.
2. Add **API_KEY** with your API key.
3. Restart the Hugging Face Space.

###  🔹 Test Your App on Hugging Face
Enter a company name (e.g., Tesla, Google).
Click "Fetch News & Analyze".
Make sure it:
✅ Fetches at least 10 news articles
✅ Displays article titles & summaries
✅ Performs sentiment analysis
✅ Shows sentiment distribution (Positive, Neutral, Negative)
✅ Generates Hindi audio output
