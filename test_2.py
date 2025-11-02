from core.fetcher import extract_text_from_url
from core.summarizer import summarize_text
from core.sentiment import get_sentiment, sentiment_label

url = "https://www.bbc.com/news/articles/cdjrymnx1e8o"

print("\nFetching article...")
article = extract_text_from_url(url)

if not article["success"]:
    print("❌ Fetch failed:", article["error"])
    exit()

text = article["text"]
print("✅ Article fetched")
print("Title:", article["title"])
print("Characters:", len(text))

print("\nSummarizing...")
summary = summarize_text(text)
print("✅ Summary:\n", summary)

print("\nAnalyzing sentiment...")
scores = get_sentiment(text)
label = sentiment_label(scores)

print("✅ Sentiment result:")
print("Label:", label)
print("Scores:", scores)
