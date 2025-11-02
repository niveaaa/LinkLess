from core.fetcher import extract_text_from_url

test_url = "https://www.bbc.com/news/science-environment-68006825"
result = extract_text_from_url(test_url)

print(result["title"])
print(result["text"][:500])  # preview first 500 chars
