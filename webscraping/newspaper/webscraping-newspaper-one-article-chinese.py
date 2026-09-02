from newspaper import Article

article = Article('https://www.bbc.com/zhongwen/simp/chinese-news-67084358')
article.download()
article.parse()

print(article.title)
# 晶片大战：台湾厂商助攻华为突破美国封锁？

if article.config.use_meta_language:
  # If we use the autodetected language, this config attribute will be true
  print(article.meta_lang)
else:
  print(article.config.language)
