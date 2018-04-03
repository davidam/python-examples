#!/usr/bin/python
# -*- coding: utf-8 -*-

from osmapi import OsmApi
MyApi = OsmApi()
print(MyApi.NodeGet(1))
