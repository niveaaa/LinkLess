from core.fetcher import extract_text_from_url
from core.summarizer import summarize_text
from core.keywords import extract_keywords

url = "https://www.bbc.com/news/articles/cdjrymnx1e8o"
result = extract_text_from_url(url)

if result["success"]:
    print("\nKEYWORDS:")
    for k in extract_keywords(result["text"]):
        print("-", k)
else:
    print("FETCH ERROR:", result["error"])
