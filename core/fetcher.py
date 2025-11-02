# core/fetcher.py

from newspaper import Article

def extract_text_from_url(url: str) -> dict:
    """
    Fetches the main text content from a given URL.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()

        if not article.text.strip():
            return {
                "success": False,
                "title": None,
                "text": None,
                "error": "No readable text found."
            }

        return {
            "success": True,
            "title": article.title or "Untitled",
            "text": article.text
        }
    
    except Exception as e:
        return {
            "success": False,
            "title": None,
            "text": None,
            "error": str(e)
        }
