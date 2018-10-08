#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.datasets import fetch_lfw_people
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

for name in lfw_people.target_names:
    print(name)
