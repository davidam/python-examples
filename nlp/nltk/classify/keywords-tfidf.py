from nltk.corpus import reuters
import math
print(reuters.fileids())         # The list of file names inside the corpus
print(len(reuters.fileids()))            # Number of files in the corpus = 10788
 
# Print the categories associated with a file
print(reuters.categories('training/999'))        # [u'interest', u'money-fx']
 
# Print the contents of the file
print(reuters.raw('test/14829'))

from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize
from collections import defaultdict
from six import string_types

stop_words = stopwords.words('english') + list(punctuation)
 
def tokenize(text):
    words = word_tokenize(text)
    words = [w.lower() for w in words]
    return [w for w in words if w not in stop_words and not w.isdigit()]

# build the vocabulary in one pass
vocabulary = set()
for file_id in reuters.fileids():
    words = tokenize(reuters.raw(file_id))
    vocabulary.update(words)
 
vocabulary = list(vocabulary)
word_index = {w: idx for idx, w in enumerate(vocabulary)}
 
VOCABULARY_SIZE = len(vocabulary)
DOCUMENTS_COUNT = len(reuters.fileids())
 
print(VOCABULARY_SIZE, DOCUMENTS_COUNT)

word_idf = defaultdict(lambda: 0)
for file_id in reuters.fileids():
    words = set(tokenize(reuters.raw(file_id)))
    for word in words:
        word_idf[word] += 1
 
for word in vocabulary:
    word_idf[word] = math.log(DOCUMENTS_COUNT / float(1 + word_idf[word]))
 
print(word_idf['deliberations'])     # 7.49443021503
print(word_idf['committee'])     # 3.61286641709

import numpy as np
 
word_idf = np.zeros(VOCABULARY_SIZE)
for file_id in reuters.fileids():
    words = set(tokenize(reuters.raw(file_id)))
    indexes = [word_index[word] for word in words]
    word_idf[indexes] += 1.0
 
word_idf = np.log(DOCUMENTS_COUNT / (1 + word_idf).astype(float))
print(word_idf[word_index['deliberations']])     # 7.49443021503
print(word_idf[word_index['committee']])         # 3.61286641709

def word_tf(word, document):
    if isinstance(document, string_types):
        document = tokenize(document)
 
    return float(document.count(word)) / len(document)
 
def tf_idf(word, document):
    # If not tokenized
    if isinstance(document, string_types):
        document = tokenize(document)
 
    if word not in word_index:
        return .0
 
    return word_tf(word, document) * word_idf[word_index[word]]

print(tf_idf('year', reuters.raw('test/14829')))                 # 0.0209031169481
print(tf_idf('following', reuters.raw('test/14829')))            # 0.0306117802726
print(tf_idf('provided', reuters.raw('test/14829')))             # 0.0388082713404
print(tf_idf('structural', reuters.raw('test/14829')))           # 0.0534999300236
print(tf_idf('japanese', reuters.raw('test/14829')))             # 0.0613707825494
print(tf_idf('downtrend', reuters.raw('test/14829')))            # 0.068131183773


from sklearn.feature_extraction.text import TfidfVectorizer
 
tfidf = TfidfVectorizer(stop_words=stop_words, tokenizer=tokenize, vocabulary=vocabulary)
 
# Fit the TfIdf model
tfidf.fit([reuters.raw(file_id) for file_id in reuters.fileids()])
 
# Transform a document into TfIdf coordinates
X = tfidf.transform([reuters.raw('test/14829')])
 
 
# Check out some frequencies
print(X[0, tfidf.vocabulary_['year']])                  # 0.0562524229373
print(X[0, tfidf.vocabulary_['following']])             # 0.057140265658
print(X[0, tfidf.vocabulary_['provided']])              # 0.0689364372666
print(X[0, tfidf.vocabulary_['structural']])            # 0.0900802810906
print(X[0, tfidf.vocabulary_['japanese']])              # 0.114492409303
print(X[0, tfidf.vocabulary_['downtrend']])             # 0.111137191743

from gensim.models import TfidfModel
from gensim.corpora import Dictionary
#import gensim

documents = [tokenize(reuters.raw(file_id)) for file_id in reuters.fileids()]
dictionary = Dictionary(documents) 
 
tfidf_model = TfidfModel([dictionary.doc2bow(d) for d in documents], id2word=dictionary)
tfidf_values = dict(tfidf_model[dictionary.doc2bow(tokenize(reuters.raw('test/14829')))])
 
print(tfidf_values[dictionary.token2id['year']])                    # 0.0367516096888
print(tfidf_values[dictionary.token2id['following']])               # 0.0538505795815
print(tfidf_values[dictionary.token2id['provided']])                # 0.0683210467787
print(tfidf_values[dictionary.token2id['structural']])              # 0.0945807226371
print(tfidf_values[dictionary.token2id['japanese']])                # 0.107960637598
print(tfidf_values[dictionary.token2id['downtrend']])                # 0.122670341446
