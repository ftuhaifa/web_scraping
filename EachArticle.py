# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:33:50 2024

@author: Fatimah Altuhaifa
"""

import newspaper
import json

url = 'https://www.arabnews.com/node/2327891/corporate-news'
  
article = newspaper.Article(url=url, language='en')
article.download()
article.parse()


article ={
    "title": str(article.title),
    "text": str(article.text),
    "authors": article.authors,
    "published_date": str(article.publish_date),
    "top_image": str(article.top_image),
    "videos": article.movies,
    "keywords": article.keywords,
    "summary": str(article.summary)
}


print(article["title"] \
     + "\n\t\t" + article["published_date"] \
     + "\n\n"\
     + "\n" + article["text"]\
     + "\n\n")