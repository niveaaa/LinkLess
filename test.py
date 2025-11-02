from core.fetcher import extract_text_from_url

test_url = "https://www.bbc.com/news/articles/cdjrymnx1e8o"
result = extract_text_from_url(test_url)

if result["success"]:
    print("\nTITLE:", result["title"])
    print("\nTEXT PREVIEW:\n", result["text"])
else:
    print("❌ FAILED:", result["error"])