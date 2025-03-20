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

def text_to_speech(text, filename="summary.mp3"):
    tts = gTTS(text=text, lang='hi')
    tts.save(filename)
    return filename
