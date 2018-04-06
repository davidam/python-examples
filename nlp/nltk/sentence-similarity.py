from nltk.corpus import brown, stopwords
from nltk.cluster.util import cosine_distance
 
def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)
 
# One out of 5 words differ => 0.8 similarity
print(sentence_similarity("This is a good sentence".split(), "This is a bad sentence".split()))
 
# One out of 2 non-stop words differ => 0.5 similarity
print(sentence_similarity("This is a good sentence".split(), "This is a bad sentence".split(), stopwords.words('english')))
 
# 0 out of 2 non-stop words differ => 1 similarity (identical sentences)
print(sentence_similarity("This is a good sentence".split(), "This is a good sentence".split(), stopwords.words('english')))
 
# Completely different sentences=> 0.0
print(sentence_similarity("This is a good sentence".split(), "I want to go to the market".split(), stopwords.words('english')))
 
