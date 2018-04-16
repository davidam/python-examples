#!/usr/bin/python# -*- coding: utf-8 -*-

import nltk
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
    nltk.corpus.genesis.words('english-web.txt'))
finder.nbest(bigram_measures.pmi, 10)

finder.apply_freq_filter(3)
finder.nbest(bigram_measures.pmi, 10)  # doctest: +NORMALIZE_WHITESPACE

finder = BigramCollocationFinder.from_words(
    nltk.corpus.brown.tagged_words('ca01', tagset='universal'))
finder.nbest(bigram_measures.pmi, 5)  # doctest: +NORMALIZE_WHITESPACE

finder = BigramCollocationFinder.from_words(t for w, t in
    nltk.corpus.brown.tagged_words('ca01', tagset='universal'))
finder.nbest(bigram_measures.pmi, 10)  # doctest: +NORMALIZE_WHITESPACE

finder = BigramCollocationFinder.from_words(
    nltk.corpus.genesis.words('english-web.txt'),
    window_size = 20)
finder.apply_freq_filter(2)
ignored_words = nltk.corpus.stopwords.words('english')
finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
finder.nbest(bigram_measures.likelihood_ratio, 10) # doctest: +NORMALIZE_WHITESPACE

text = "I do not like green eggs and ham, I do not like them Sam I am!"
tokens = nltk.wordpunct_tokenize(text)
finder = BigramCollocationFinder.from_words(tokens)
scored = finder.score_ngrams(bigram_measures.raw_freq)
sorted(bigram for bigram, score in scored)  # doctest: +NORMALIZE_WHITESPACE

word_fd = nltk.FreqDist(tokens)
bigram_fd = nltk.FreqDist(nltk.bigrams(tokens))
finder = BigramCollocationFinder(word_fd, bigram_fd)
scored == finder.score_ngrams(bigram_measures.raw_freq)

finder = TrigramCollocationFinder.from_words(tokens)
scored = finder.score_ngrams(trigram_measures.raw_freq)
set(trigram for trigram, score in scored) == set(nltk.trigrams(tokens))

sorted(finder.nbest(trigram_measures.raw_freq, 2))

sorted(finder.above_score(trigram_measures.raw_freq,
                          1.0 / len(tuple(nltk.trigrams(tokens)))))

finder = TrigramCollocationFinder.from_words(tokens)
finder = TrigramCollocationFinder.from_words(tokens, window_size=4)
sorted(finder.nbest(trigram_measures.raw_freq, 4))

sorted(finder.ngram_fd.items(), key=lambda t: (-t[1], t[0]))[:10]  # doctest: +NORMALIZE_WHITESPACE

finder = TrigramCollocationFinder.from_words(tokens)
len(finder.score_ngrams(trigram_measures.raw_freq))
finder.apply_word_filter(lambda w: w in ('I', 'me'))
len(finder.score_ngrams(trigram_measures.raw_freq))
sorted(finder.above_score(trigram_measures.raw_freq,
                          1.0 / len(tuple(nltk.trigrams(tokens)))))

finder.apply_ngram_filter(lambda w1, w2, w3: 'and' in (w1, w3))
len(finder.score_ngrams(trigram_measures.raw_freq))

finder.apply_freq_filter(2)
len(finder.score_ngrams(trigram_measures.raw_freq))

# Association measures

print('%0.4f' % bigram_measures.student_t(8, (15828, 4675), 14307668))
print('%0.4f' % bigram_measures.student_t(20, (42, 20), 14307668))

print('%0.2f' % bigram_measures.chi_sq(8, (15828, 4675), 14307668))
print('%0.0f' % bigram_measures.chi_sq(59, (67, 65), 571007))

print('%0.2f' % bigram_measures.likelihood_ratio(110, (2552, 221), 31777))
print('%0.2f' % bigram_measures.likelihood_ratio(8, (13, 32), 31777))

print('%0.2f' % bigram_measures.pmi(20, (42, 20), 14307668))
print('%0.2f' % bigram_measures.pmi(20, (15019, 15629), 14307668))

# Using contingency table values

from nltk.metrics import ContingencyMeasures
cont_bigram_measures = ContingencyMeasures(bigram_measures)
print('%0.2f' % cont_bigram_measures.likelihood_ratio(8, 5, 24, 31740))
print('%0.2f' % cont_bigram_measures.chi_sq(8, 15820, 4667, 14287173))

# Ranking and correlation

from nltk.metrics.spearman import *
results_list = ['item1', 'item2', 'item3', 'item4', 'item5']
print(list(ranks_from_sequence(results_list)))

results_scored = [('item1', 50.0), ('item2', 40.0), ('item3', 38.0),
                  ('item4', 35.0), ('item5', 14.0)]
print(list(ranks_from_scores(results_scored, rank_gap=5)))
[('item1', 0), ('item2', 1), ('item3', 1), ('item4', 1), ('item5', 4)]

print('%0.1f' % spearman_correlation(
        ranks_from_sequence(results_list),
        ranks_from_sequence(results_list)))

print('%0.1f' % spearman_correlation(
        ranks_from_sequence(reversed(results_list)),
        ranks_from_sequence(results_list)))

results_list2 = ['item2', 'item3', 'item1', 'item5', 'item4']
print('%0.1f' % spearman_correlation(
       ranks_from_sequence(results_list),
       ranks_from_sequence(results_list2)))

print('%0.1f' % spearman_correlation(
       ranks_from_sequence(reversed(results_list)),
       ranks_from_sequence(results_list2)))
