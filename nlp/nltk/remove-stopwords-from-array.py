
import nltk
from nltk import wordpunct_tokenize
from nltk.corpus import brown, stopwords
from nltk.cluster.util import cosine_distance
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import cmudict

array = ["All", "work", "and", "no", "play", "makes", "jack", "dull", "boy.", "All", "work", "and", "no", "play", "makes", "jack", "a", "dull", "boy", "."]
print("With stop words")
print(array)
stopWords = set(stopwords.words('english'))

wordsFiltered = []

for w in array:
    if w not in stopWords:
        wordsFiltered.append(w)

print("Without stop words")        
print(wordsFiltered)
