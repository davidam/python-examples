#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: David Arroyo Menéndez. All rights reserved.
# Natural Language Toolkit: code_gender_features_overfitting


from pygithub3 import Github
from pprint import pprint
import subprocess


user='davidam'
gh = Github(login=user, password='lala')

davidam = gh.users.get() # Auth required

for name in dir(gh):
    print(name)

#pprint(gh.repos.list().all())
for r in gh.repos.list().all():
#    print r.name
    strgit = "git clone http://github.com/"+user+"/"+r.name+".git"
    print(strgit)
    subprocess.call(strgit, shell=True)

# other repositories
subprocess.call("git clone https://code.orgmode.org/bzg/org-mode.git", shell=True)
subprocess.call("git clone git://orgmode.org/worg.git", shell=True)
