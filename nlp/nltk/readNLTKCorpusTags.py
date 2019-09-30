import nltk

tagged_sentence = nltk.corpus.treebank.tagged_sents(tagset='universal')
print("Number of Tagged Sentences ",len(tagged_sentence))
tagged_words=[tup for sent in tagged_sentence for tup in sent]
print("Total Number of Tagged words", len(tagged_words))
vocab=set([word for word,tag in tagged_words])
print("Vocabulary of the Corpus",len(vocab))
tags=set([tag for word,tag in tagged_words])
print("Number of Tags in the Corpus ",len(tags))
