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

# Count commits
# You can execute this script following this tutorial:
# https://grimoirelab.gitbooks.io/training/perceval/first_steps.html
# source ~/venvs/perceval/bin/activate 
# $ python3 ~/git/python-examples/perceval/perceval_git_counter_sexmachine.py https://github.com/grimoirelab/perceval.git /tmp/clonedir



import argparse
from pprint import pprint
from perceval.backends.core.git import Git
import nltk
import re


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

# Read command line arguments
parser = argparse.ArgumentParser(description = "Count commits in a git repo")
parser.add_argument("repo", help = "Repository url")
parser.add_argument("dir", help = "Directory for cloning the repository")
parser.add_argument("--print", action='store_true', help = "Print hashes")
args = parser.parse_args()

# create a Git object, and count commmits
repo = Git(uri=args.repo, gitpath=args.dir)
countcommit = 0
countuser = 0
pprint(repo)

for commit in repo.fetch():
    if args.print:
        print(commit['data']['commit'])
    countcommit += 1

males = 0
females = 0
for user in repo.fetch():
    str1 = user['data']['Author']
    m = re.match("(\w+)", str1)
    user_name = m.group(0) 
    if (classifier.classify(gender_features(user_name)) == 'male'):
        males += 1
    elif (classifier.classify(gender_features(user_name)) == 'female'):    
        females += 1
    countuser += 1

print("Number of commits sended by males: %d." % (males))
print("Number of commits sended by females: %d." % (females))    
print("Number of commmits: %d." % (countcommit))

