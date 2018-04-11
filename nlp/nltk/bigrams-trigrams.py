from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict
 
first_sentence = reuters.sents()[0]
print(first_sentence) # [u'ASIAN', u'EXPORTERS', u'FEAR', u'DAMAGE', u'FROM' ...
 
# Get the bigrams
print("\n+++++++++++++ BIGRAMS ++++++++++++++++++++++\n")
print(list(bigrams(first_sentence))) # [(u'ASIAN', u'EXPORTERS'), (u'EXPORTERS', u'FEAR'), (u'FEAR', u'DAMAGE'), (u'DAMAGE', u'FROM'), ...
 
# Get the padded bigrams
print(list(bigrams(first_sentence, pad_left=True, pad_right=True))) # [(None, u'ASIAN'), (u'ASIAN', u'EXPORTERS'), (u'EXPORTERS', u'FEAR'), (u'FEAR', u'DAMAGE'), (u'DAMAGE', u'FROM'),
 
# Get the trigrams
print("\n++++++++++++ TRIGRAMS ++++++++++++++++++++++\n")
print(list(trigrams(first_sentence))) # [(u'ASIAN', u'EXPORTERS', u'FEAR'), (u'EXPORTERS', u'FEAR', u'DAMAGE'), (u'FEAR', u'DAMAGE', u'FROM'), ...
 
# Get the padded trigrams
print(list(trigrams(first_sentence, pad_left=True, pad_right=True))) # [(None, None, u'ASIAN'), (None, u'ASIAN', u'EXPORTERS'), (u'ASIAN', u'EXPORTERS', u'FEAR'), (u'EXPORTERS', u'FEAR', u'DAMAGE'), (u'FEAR', u'DAMAGE', u'FROM') ...
 
