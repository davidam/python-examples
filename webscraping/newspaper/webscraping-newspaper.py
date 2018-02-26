#!/usr/bin/python3

from newspaper import Article

url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
article = Article(url)
article.download()

print(article.html)

article.parse()

article.authors

article.publish_date

article.text

article.top_image

article.movies

print(article.nlp())

article.keywords

print(article.summary)

import newspaper

elpais = newspaper.build('http://www.elpais.com')
print("number of articles in elpais")
print(len(elpais.articles))

# for article in cnn_paper.articles:
#     print(article.url)

# for category in cnn_paper.category_urls():
#     print(category)

    
# cnn_article = cnn_paper.articles[0]
# print(cnn_article)
# cnn_article.download()
# cnn_article.parse()
# cnn_article.nlp()

