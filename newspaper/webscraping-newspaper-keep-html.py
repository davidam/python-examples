from newspaper import Article

a = Article('http://www.cnn.com/2014/01/12/world/asia/north-korea-charles-smith/index.html', keep_article_html=True)
a.download()
a.parse()
print(a.article_html)
