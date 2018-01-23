#! /usr/bin/env python3
# Print messages
# You can execute this script following this tutorial:
# https://grimoirelab.gitbooks.io/tutorial/content/before-you-start/installing-grimoirelab.html
# https://grimoirelab.gitbooks.io/tutorial/content/perceval/mail.html
# source ~/venvs/mordred/bin/activate

# from pprint import pprint
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
mbox_uri = 'http://mail-archives.apache.org/mod_mbox/httpd-announce/'
# directory for letting Perceval where mbox archives are
# you need to have the archives to analyzed there before running the script
mbox_dir = 'archives'

# create a mbox object, using mbox_uri as label, mbox_dir as directory to scan
repo = MBox(uri=mbox_uri, dirpath=mbox_dir)
# fetch all messages as an iteratoir, and print first 60 chars for each subject
for message in repo.fetch():
    print('Subject')
    print(message['data']['Subject'][0:59])
    print('unixfrom')
    print(message['data']['From'])
    print(classifier.classify(gender_features(message['data']['From'])))
#    pprint(message['data'])
