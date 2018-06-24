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

from github import Github
import subprocess
import os
import getpass

os.chdir("/home/davidam/gittest")

user = "davidam"
# using username and password
passw = getpass.getpass("Give me your password: ") 
g = Github(user, passw)

# or using an access token
#g = Github("access_token")

for repo in g.get_user().get_repos():
    print(repo.name)
    strgit = "git clone http://github.com/"+user+"/"+repo.name+".git"
    print(strgit)
    subprocess.call(strgit, shell=True)    


# orgmode repositories
subprocess.call("git clone https://code.orgmode.org/bzg/org-mode.git", shell=True)
subprocess.call("git clone git://orgmode.org/worg.git", shell=True)
# savannah repositories
os.chdir("/home/davidam/bzr")
subprocess.call("bzr branch bzr+ssh://"+user+"@bzr.savannah.nongnu.org/drupal-el", shell=True)
subprocess.call("bzr branch bzr+ssh://"+user+"@bzr.savannah.nongnu.org/gccintro-es", shell=True)

os.chdir("/home/davidam/git")
subprocess.call("git clone "+user+"@git.sv.gnu.org:/srv/git/elisp-es.git", shell=True)
subprocess.call("git clone "+user+"@git.sv.gnu.org:/srv/git/php-ext-el.git", shell=True)

# drupal repositories
os.chdir("/home/davidam/git/drupal/7")
subprocess.call("git clone --branch 7.x-1.x "+ user +"@git.drupal.org:project/orgmode.git", shell=True)
subprocess.call("git clone --branch 7.x-1.x "+ user +"@git.drupal.org:project/ocrad.git", shell=True)

os.chdir("/home/davidam/git/drupal/8")
subprocess.call("git clone --branch 8.x-1.x "+ user +"@git.drupal.org:project/orgmode.git", shell=True)
subprocess.call("git clone --branch 8.x-1.x "+ user +"@git.drupal.org:project/ocrad.git", shell=True)
    
