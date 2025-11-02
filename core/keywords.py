# core/keywords.py

from rake_nltk import Rake
import nltk
import re

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

def extract_keywords(text: str, max_keywords: int = 8) -> list:
    rake = Rake()
    rake.extract_keywords_from_text(text)
    phrases = rake.get_ranked_phrases()

    cleaned = []
    for p in phrases:
        p = p.strip().lower()
        if len(p) < 4: 
            continue
        if len(p.split()) > 4:
            continue
        if re.search(r"\d", p):
            continue
        cleaned.append(p)

    return cleaned[:max_keywords] if cleaned else ["(No good keywords found)"]
