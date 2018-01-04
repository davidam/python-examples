#!/usr/bin/python3

import newspaper
#from newspaper import Article

#cnn_paper = newspaper.build('http://cnn.com')
lemonde_paper = newspaper.build('http://www.lemonde.fr')
for article in lemonde_paper.articles:
    print(article.url)
    
for category in lemonde_paper.category_urls():
    print(category)

article = lemonde_paper.articles[0]
article.download()
#print(article.html)
article.parse()
print(article.authors)
print(article.text)
print(article.top_image)
print(article.movies)

article.nlp()
print("KEYWORDS")
print(article.keywords)
print("SUMMARY")
print(article.summary)

#first_article = Article(url="http://www.lemonde.fr", language='fr')
#first_article = cnn_paper.articles[0]
#first_article.download()
#first_article.nlp()
# print(first_article.summary)
# print(first_article.keywords)
#print(cnn_paper.articles[100].nlp())

