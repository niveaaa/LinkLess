import streamlit as st
from core.fetcher import extract_text_from_url
from core.summarizer import summarize_text
from core.sentiment import get_sentiment, sentiment_label

st.set_page_config(page_title="LinkLess", layout="wide")

st.title("🔗 LinkLess – Read Smarter, Faster")

url = st.text_input("Enter article URL:")

if st.button("Process"):
    if not url.strip():
        st.error("Please enter a valid URL.")
    else:
        with st.spinner("Fetching article..."):
            article = extract_text_from_url(url)

        if not article["success"]:
            st.error(f"Failed to fetch article: {article['error']}")
        else:
            text = article["text"]
            title = article["title"]

            st.success("Article fetched successfully!")
            st.subheader(title)

            # Summary
            summary = summarize_text(text)
            st.markdown("### 🧠 Summary")
            st.write(summary)

            # Sentiment
            scores = get_sentiment(text)
            label = sentiment_label(scores)

            color = {
                "POSITIVE": "green",
                "NEGATIVE": "red",
                "NEUTRAL": "gray"
            }.get(label, "gray")

            st.markdown(f"### 📌 Sentiment: <span style='color:{color}'>{label}</span>", unsafe_allow_html=True)

            # Toggle full text
            with st.expander("Show full extracted article text"):
                st.write(text)

            # Download button
            st.download_button(
                label="Download summary as .txt",
                data=summary,
                file_name="summary.txt"
            )
