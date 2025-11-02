from core.fetcher import extract_text_from_url
from core.summarizer import summarize_text

url = "https://www.bbc.com/news/articles/cdjrymnx1e8o"   # replace with real link
result = extract_text_from_url(url)

if result["success"]:
    bullets = summarize_text(result["text"])
    print("\nSUMMARY:")
    for b in bullets:
        print("•", b)
else:
    print("FETCH ERROR:", result["error"])
