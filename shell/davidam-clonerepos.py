#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: David Arroyo Menéndez. All rights reserved.



from pygithub3 import Github
from pprint import pprint
import subprocess
import os

os.chdir("/home/davidam/git")

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

# orgmode repositories
subprocess.call("git clone https://code.orgmode.org/bzg/org-mode.git", shell=True)
subprocess.call("git clone git://orgmode.org/worg.git", shell=True)
# savannah repositories

subprocess.call("bzr branch bzr+ssh://davidam@bzr.savannah.nongnu.org/drupal-el", shell=True)
subprocess.call("bzr branch bzr://bzr.savannah.nongnu.org/gccintro-es", shell=True)
subprocess.call("git clone davidam@git.sv.gnu.org:/srv/git/elisp-es.git", shell=True)
subprocess.call("git clone davidam@git.sv.gnu.org:/srv/git/php-ext-el.git", shell=True)
# drupal repositories
subprocess.call("git clone --branch 7.x-1.x davidam@git.drupal.org:project/orgmode.git", shell=True)
subprocess.call("git clone --branch 7.x-1.x davidam@git.drupal.org:project/ocrad.git", shell=True)
