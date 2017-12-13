# Natural Language Toolkit: code_dictionary
# http://www.nltk.org/book/ch05.html

from collections import defaultdict
counts = defaultdict(int)

from nltk.corpus import brown
for (word, tag) in brown.tagged_words(categories='news', tagset='universal'):
    counts[tag] += 1
print counts['NOUN']
print sorted(counts)

from operator import itemgetter
print sorted(counts.items(), key=itemgetter(1), reverse=True)
print [t for t, c in sorted(counts.items(), key=itemgetter(1), reverse=True)]


