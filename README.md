# LinkLess

LinkLess is a fast web tool that takes any article URL, extracts the main content, summarizes it, and detects its sentiment (positive, negative, or neutral). No sign-ups, no clutter — just paste a link and get the key insights instantly.

---

## 🚀 Features
- 📰 **URL-based article extraction**
- ✂️ **Automatic text summarization**
- 🙂 **Sentiment analysis using VADER**
- 📄 **Downloadable summary (.txt)**
- 🎨 **Simple and responsive Streamlit UI**

---

## 🛠️ Tech Stack
- **Python 3**
- **newspaper3k** – article scraping
- **NLTK + VADER** – sentiment analysis
- **Streamlit** – UI
- **Sumy** – text summarization

---

## 📦 Installation

```bash
git clone https://github.com/your-username/LinkLess.git
cd LinkLess
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```bash
LinkLess/
│── app.py                # Streamlit UI
│── core/
│   ├── extract.py        # URL article extraction
│   ├── sentiment.py      # Sentiment analysis
│   └── summarizer.py     # Text summarization
│── requirements.txt
│── README.md
```

---

## 🔮 Future Add-Ons
- Multi-language support
- Fake-news / credibility score
- Browser extension version
- Export to PDF & Markdown

---

## 👤 Author
Built by nivea during a caffeine-powered dev sprint.
PRs welcome. Bugs expected. Vibes immaculate.
