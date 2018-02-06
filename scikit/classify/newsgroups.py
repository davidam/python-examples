from sklearn.datasets import fetch_20newsgroups
news = fetch_20newsgroups(subset='all')
 
print len(news.data)
# 18846
 
print len(news.target_names)
# 20
 
print news.target_names
# ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']
 
for text, num_label in zip(news.data[:10], news.target[:10]):
    print '[%s]:\t\t "%s ..."' % (news.target_names[num_label], text[:100].split('\n')[0])
