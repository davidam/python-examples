#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://api.mongodb.com/python/current/tutorial.html

from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client.test_database

print("The database (db) is:")
pprint(db)

collection = db.test_collection

print("The collection is:")
pprint(collection)

import datetime
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

print("The post is:")
pprint(post)

# You need mongo 2.6 to run this part:
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# print("The post id inserted is:")
# pprint(post_id)

# pprint(db.collection_names(include_system_collections=False))

# pprint(posts.find_one())
# pprint(posts.find_one({"author": "Mike"}))
