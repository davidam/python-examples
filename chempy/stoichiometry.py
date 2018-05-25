#!/usr/bin/python
# -*- coding: utf-8 -*-

from chempy import balance_stoichiometry  # Main reaction in NASA's booster rockets:
reac, prod = balance_stoichiometry({'NH4ClO4', 'Al'}, {'Al2O3', 'HCl', 'H2O', 'N2'})
from pprint import pprint
pprint(dict(reac))
pprint(dict(prod))
from chempy import mass_fractions
for fractions in map(mass_fractions, [reac, prod]):
    pprint({k: '{0:.3g} wt%'.format(v*100) for k, v in fractions.items()})
