#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# Print messages
# You can execute this script following this tutorial:
# https://chaoss.github.io/grimoirelab-tutorial/
# source ~/venvs/mordred/bin/activate

# from pprint import pprint
from perceval.backends.core.git import Git
from perceval.backends.core.mbox import MBox
from pprint import pprint
import nltk

def gender_features(name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)


# uri (label) for the mailing list to analyze
mbox_uri = 'ftp://lists.gnu.org/emacs-devel/'

# directory for letting Perceval where mbox archives are
# you need to have the archives to analyzed there before running the script
mbox_dir = 'archives'

# create a mbox object, using mbox_uri as label, mbox_dir as directory to scan
repo = MBox(uri=mbox_uri, dirpath=mbox_dir)
# fetch all messages as an iterator, and print first 60 chars for each subject
males = 0
females = 0
for message in repo.fetch():
    print('Subject')
    print(message['data']['Subject'][0:59])
    print('unixfrom')
    print(message['data']['From'])
    gender = classifier.classify(gender_features(message['data']['From']))
    print(gender)
    if (gender == 'male'):
        males = males + 1
    if (gender == 'female'):
        females = females + 1

print("The number of messages of females is " + str(females))
print("The number of messages of males is " + str(males))
#    pprint(message['data'])
