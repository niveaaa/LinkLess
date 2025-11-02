# core/keywords.py

from rake_nltk import Rake
import nltk

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

def extract_keywords(text: str, max_keywords: int = 8) -> list:
    
    try:
        rake = Rake()
        rake.extract_keywords_from_text(text)
        ranked = rake.get_ranked_phrases()

        if not ranked:
            return ["(No keywords found)"]

        return ranked[:max_keywords]

    except Exception as e:
        return [f"(Error extracting keywords: {e})"]
