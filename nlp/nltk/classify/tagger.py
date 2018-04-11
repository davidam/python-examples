#!/usr/bin/python# -*- coding: utf-8 -*-
import pickle
from collections import Iterable
from nltk import ChunkParserI, ClassifierBasedTagger
from nltk.stem.snowball import SnowballStemmer

import random
from nltk.chunk import conlltags2tree, tree2conlltags

from nltk.corpus import conll2000

#http://nlpforhackers.io/text-chunking/

chunked_sentence = conll2000.chunked_sents()[0]
print(chunked_sentence)

shuffled_conll_sents = list(conll2000.chunked_sents())
random.shuffle(shuffled_conll_sents)
train_sents = shuffled_conll_sents[:int(len(shuffled_conll_sents) * 0.9)]
test_sents = shuffled_conll_sents[int(len(shuffled_conll_sents) * 0.9 + 1):]

def features(tokens, index, history):
    """
    `tokens`  = a POS-tagged sentence [(w1, t1), ...]
    `index`   = the index of the token we want to extract features for
    `history` = the previous predicted IOB tags
    """
 
    # init the stemmer
    stemmer = SnowballStemmer('english')
 
    # Pad the sequence with placeholders
    tokens = [('__START2__', '__START2__'), ('__START1__', '__START1__')] + list(tokens) + [('__END1__', '__END1__'), ('__END2__', '__END2__')]
    history = ['__START2__', '__START1__'] + list(history)
 
    # shift the index with 2, to accommodate the padding
    index += 2
 
    word, pos = tokens[index]
    prevword, prevpos = tokens[index - 1]
    prevprevword, prevprevpos = tokens[index - 2]
    nextword, nextpos = tokens[index + 1]
    nextnextword, nextnextpos = tokens[index + 2]
 
    return {
        'word': word,
        'lemma': stemmer.stem(word),
        'pos': pos,
 
        'next-word': nextword,
        'next-pos': nextpos,
 
        'next-next-word': nextnextword,
        'nextnextpos': nextnextpos,
 
        'prev-word': prevword,
        'prev-pos': prevpos,
 
        'prev-prev-word': prevprevword,
        'prev-prev-pos': prevprevpos,
    }
 
 
class ClassifierChunkParser(ChunkParserI):
    def __init__(self, chunked_sents, **kwargs):
        assert isinstance(chunked_sents, Iterable)
 
        # Transform the trees in IOB annotated sentences [(word, pos, chunk), ...]
        chunked_sents = [tree2conlltags(sent) for sent in chunked_sents]
 
        # Transform the triplets in pairs, make it compatible with the tagger interface [((word, pos), chunk), ...]
        def triplets2tagged_pairs(iob_sent):
            return [((word, pos), chunk) for word, pos, chunk in iob_sent]
        chunked_sents = [triplets2tagged_pairs(sent) for sent in chunked_sents]
 
        self.feature_detector = features
        self.tagger = ClassifierBasedTagger(
            train=chunked_sents,
            feature_detector=features,
            **kwargs)
 
    def parse(self, tagged_sent):
        chunks = self.tagger.tag(tagged_sent)
 
        # Transform the result from [((w1, t1), iob1), ...] 
        # to the preferred list of triplets format [(w1, t1, iob1), ...]
        iob_triplets = [(w, t, c) for ((w, t), c) in chunks]
 
        # Transform the list of triplets to nltk.Tree format
        return conlltags2tree(iob_triplets)
 
classifier_chunker = ClassifierChunkParser(train_sents)
print(classifier_chunker.evaluate(test_sents))
