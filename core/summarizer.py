# core/summarizer.py

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

import nltk

def summarize_text(text: str, sentence_count: int = 10) -> list:

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        try:
            nltk.download("punkt", quiet=True)
        except:
            pass

    try:
        nltk.data.find("tokenizers/punkt_tab")
    except LookupError:
        try:
            nltk.download("punkt_tab", quiet=True)
        except:
            pass
   
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentence_count)

        bullets = [str(sentence) for sentence in summary]
        return bullets if bullets else ["(Summary could not be generated)"]
    
    except Exception as e:
        return [f"(Error generating summary: {e})"]
