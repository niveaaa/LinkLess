# core/sentiment.py

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text: str) -> dict:
    
    try:
        scores = analyzer.polarity_scores(text)
        return scores
    except Exception as e:
        return {"error": str(e)}

def sentiment_label(scores: dict) -> str:
    
    if "compound" not in scores:
        return "ERROR"
    c = scores["compound"]
    if c >= 0.05:
        return "POSITIVE"
    elif c <= -0.05:
        return "NEGATIVE"
    return "NEUTRAL"
