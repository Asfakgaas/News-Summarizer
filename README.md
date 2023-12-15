# News Summarizer with Streamlit

![License](https://img.shields.io/badge/license-MIT-blue.svg)

This project is a simple news summarizer implemented as a Streamlit app. It allows users to summarize news articles from either a provided URL or by pasting the news text directly into the app.

## Features

- Summarize news articles from a URL.
- Summarize news articles by pasting the news text.


## Getting Started

### Prerequisites

Make sure you have Python 3.10.6 installed.

### Installation

Clone the repository:

```bash
git clone https://github.com/Kirrishz/news-summarizer.git
cd news-summarizer
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run summarizer.py
    ```

2. Open the provided URL in your web browser.

3. Choose the summarization type (URL or Text) from the sidebar.

4. Enter the news URL or paste the news text.

5. Click the "Summarize" button to view the original news content and its summary.

## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/new-feature`.
3. Make your changes and commit them: `git commit -m "Add new feature"`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://www.streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Newspaper3k](https://newspaper.readthedocs.io/en/latest/)
