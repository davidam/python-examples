#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: David Arroyo Menéndez. All rights reserved.
# Natural Language Toolkit: code_gender_features_overfitting

import nltk
import pickle
def gender_features(name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

nombre1 = input("What's your name?: ")
nombre2 = input("What's my name?: ")

#print gender_features('John')

from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

if ((nombre1, "female") in labeled_names):
    str1 = nombre1 + " is female"
elif ((nombre1, "male") in labeled_names):
    str1 = nombre1 + " is male"
else:
    str1 = nombre1 + " is " + classifier.classify(gender_features(nombre1))

if ((nombre2, "female") in labeled_names):
    str2 = nombre2 + " is female"
elif ((nombre2, "male") in labeled_names):
    str2 = nombre2 + " is male"
else:
    str2 = nombre2 + " is " + classifier.classify(gender_features(nombre2))

string = str1 + " and " + str2 + ". Enjoy!."

if (("female" in string) and ("male" in string)):
    print(string)

print("The classifier has an accuracy: " + str(nltk.classify.accuracy(classifier, test_set)))
print("The most informative features are: " + str(classifier.show_most_informative_features(5)))

save_classifier = open("sexmachine.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
