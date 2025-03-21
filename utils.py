from textblob import TextBlob
from gtts import gTTS
from deep_translator import GoogleTranslator

# Sentiment Analysis Function
def analyze_sentiment(text):
    """Analyze sentiment of a given text using TextBlob."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Hindi Text-to-Speech Function
def text_to_speech(text):
    """Convert text to Hindi speech using gTTS."""
    try:
        translated_text = GoogleTranslator(source='en', target='hi').translate(text)
        tts = gTTS(text=translated_text, lang='hi')
        tts.save("summary.mp3")
        return "summary.mp3"
    except Exception as e:
        return None  # No Streamlit dependency

# Text Translation Function
def translate_text(text):
    """Translate English text to Hindi."""
    try:
        return GoogleTranslator(source='en', target='hi').translate(text)
    except Exception:
        return "Translation Error"
