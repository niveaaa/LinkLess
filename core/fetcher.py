# core/fetcher.py

from newspaper import Article

def extract_text_from_url(url: str) -> dict:
    """
    {
        "title": "...",
        "text": "...",
        "success": True/False,
        "error": "...",
    }
    """
    try:
        article = Article(url)
        article.download()
        article.parse()

        if not article.text.strip():
            return {"success": False, "error": "No readable text found."}

        return {
            "success": True,
            "title": article.title,
            "text": article.text
        }
    
    except Exception as e:
        return {"success": False, "error": str(e)}
