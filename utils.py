from textblob import TextBlob
from gtts import gTTS
import os

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def text_to_speech(text):
    try:
        translated_text = GoogleTranslator(source='en', target='hi').translate(text)
        tts = gTTS(text=translated_text, lang='hi')
        tts.save("summary.mp3")
        return "summary.mp3"
    
    except Exception as e:
        st.error(f"Error in text-to-speech: {e}")
        return None
