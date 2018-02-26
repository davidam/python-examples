import newspaper

cbs_paper = newspaper.build('http://cbs.com', memoize_articles=False)
#print cbs_paper.size()
cnn_paper = newspaper.build('http://cnn.com')

for category in cnn_paper.category_urls():
    print(category)

for feed_url in cnn_paper.feed_urls():
    print(feed_url)

print(cnn_paper.brand)

print(cnn_paper.description)

first_article = cnn_paper.articles[0]
print(len(cnn_paper.articles))

# from newspaper import Article
# first_article = Article(url="http://www.lemonde.fr/...", language='fr')

# first_article = cnn_paper.articles[0]

# first_article.download()

# print(first_article.html)
#print(cnn_paper.articles[7].html)
