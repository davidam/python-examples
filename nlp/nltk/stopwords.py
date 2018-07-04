import nltk
from nltk.corpus import stopwords

print(stopwords.words('english'))
print(stopwords.words('spanish'))

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('spanish')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

print("The content fraction of the sentence is: %s" % content_fraction("En un lugar de la Mancha de cuyo nombre no quiero acordarme"))
