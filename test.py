from core.fetcher import extract_text_from_url
from core.sentiment import get_sentiment

url = "https://www.bbc.com/news/articles/cdjrymnx1e8o"
article = extract_text_from_url(url)

if article["success"]:
    sentiment = get_sentiment(article["text"])
    print("Sentiment:", sentiment)
else:
    print("Fetch failed:", article["error"])
