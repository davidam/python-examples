#!/usr/bin/python
# -*- coding: utf-8 -*-

# If you bet on "red" at roulette, you have chance 18/38 of winning. Suppose you make a sequence of independent bets on “red” at roulette, with the decision that you will stop playing once you have won 5 times. What is the chance that after 15 bets you are still playing?

# We use binomial probability mass function. To calculate the probability, you have to estimate the probability of having up to 4 successful bets after the 15th. So the final probability will be the sum of the probability to get 0 successful bets in 15 bets, plus the probability to get 1 successful bet, ..., to the probability of having 4 successful bets in 15 bets.

import scipy.stats as ss

n = 15         # Number of total bets
p = 18./38     # Probability of getting "red" at the roulette
max_sbets = 4  # Maximum number of successful bets

hh = ss.binom(n, p)

total_p = 0
for k in range(1, max_sbets + 1):  # DO NOT FORGET THAT THE LAST INDEX IS NOT USED
    total_p += hh.pmf(k)
