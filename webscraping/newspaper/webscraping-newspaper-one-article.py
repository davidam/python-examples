import newspaper

article = newspaper.article('https://edition.cnn.com/2023/10/29/sport/nfl-week-8-how-to-watch-spt-intl/index.html')

print(article.authors)
# ['Hannah Brewitt']

print(article.publish_date)
# 2023-10-29 09:00:15.717000+00:00

print(article.text)
# New England Patriots head coach Bill Belichick, right, embraces Buffalo Bills head coach Sean McDermott ...

print(article.top_image)
# https://media.cnn.com/api/v1/images/stellar/prod/231015223702-06-nfl-season-gallery-1015.jpg?c=16x9&q=w_800,c_fill

print(article.movies)
# []

article.nlp()
print(article.keywords)
# ['patrick', 'mahomes', 'history', 'nfl', 'week', 'broncos', 'denver', 'p', 'm', '00', 'pittsburgh',...]


print(article.summary)
