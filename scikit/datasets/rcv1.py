#!/usr/bin/python
# -*- coding: utf-8 -*-

# sklearn.datasets.fetch_rcv1 will load the following version: RCV1-v2, vectors, full sets, topics multilabels

from sklearn.datasets import fetch_rcv1
rcv1 = fetch_rcv1()

print(rcv1.data.shape)
