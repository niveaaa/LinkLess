# core/sentiment.py

from transformers import pipeline

# Initialize once
sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text: str) -> dict:
    
    try:
        result = sentiment_pipeline(text)[0]
        return {
            "label": result["label"],
            "score": round(result["score"], 3)
        }
    except Exception as e:
        return {"label": "ERROR", "score": 0.0, "error": str(e)}
