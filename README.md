#News Article Scraper using Newspaper3k
This project demonstrates how to use the newspaper3k Python library to scrape and parse news articles from a given URL. The code extracts relevant information such as the article's title, text, authors, published date, top image, videos, keywords, and summary. The extracted data is then formatted into a structured JSON object for easy access and manipulation.

#Features:
Downloads and parses a news article from a specified URL.
#Extracts:
Article title
Full text of the article
Authors
Published date
Top image
Embedded videos
Keywords
Summary
Outputs the article title, published date, and full text for display.
#Dependencies:
newspaper3k
json
#How to Use:
Install the newspaper3k library using pip install newspaper3k.
Modify the url variable in the script to the URL of the news article you wish to scrape.
"url = 'https://www.arabnews.com/node/2327891/corporate-news'"
Run the script, and it will download, parse, and display the extracted information.
