import streamlit as st
from transformers import TFT5ForConditionalGeneration, T5Tokenizer
from newspaper import Article

# Load T5 model and tokenizer for summarization
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = TFT5ForConditionalGeneration.from_pretrained(model_name)

# Function to summarize news from URL
def summarize_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    content = article.text
    input_ids = tokenizer.encode("summarize: " + content, return_tensors="tf", max_length=512, truncation=True)
    summary_ids = model.generate(input_ids, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids.numpy()[0], skip_special_tokens=True)
    return summary

# Function to summarize news from text
def summarize_from_text(text):
    input_ids = tokenizer.encode("summarize: " + text, return_tensors="tf", max_length=512, truncation=True)
    summary_ids = model.generate(input_ids, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids.numpy()[0], skip_special_tokens=True)
    return summary

# Streamlit app
def main():
    st.title("News Summarizer")

    st.sidebar.header("Options")
    option = st.sidebar.selectbox("Choose summarization type", ("URL", "Text"))

    if option == "URL":
        st.sidebar.subheader("Enter News URL")
        url = st.sidebar.text_input("URL:")
        if st.sidebar.button("Summarize"):
            if url:
                st.subheader("Original News Article:")
                article = Article(url)
                article.download()
                article.parse()
                st.write(article.text)

                st.subheader("Summary:")
                summary = summarize_from_url(url)
                st.write(summary)
            else:
                st.warning("Please enter a valid URL.")

    elif option == "Text":
        st.sidebar.subheader("Paste News Text")
        text = st.sidebar.text_area("Text:")
        if st.sidebar.button("Summarize"):
            if text:
                st.subheader("Original News Text:")
                st.write(text)

                st.subheader("Summary:")
                summary = summarize_from_text(text)
                st.write(summary)
            else:
                st.warning("Please enter some text to summarize.")

if __name__ == "__main__":
    main()
