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
from pygithub3 import Github

fichero = open("github.txt", "r+")
contenido = fichero.readline()

gh = Github(login='davidam', password=contenido)

davidam = gh.users.get() # Auth required
davazp = gh.users.get('davazp')
# copitux = <User (copitux)>

davidam_followers = gh.users.followers.list().all()
davazp_followers = gh.users.followers.list('davazp').all()

print("davidam followers:")
print(davidam_followers)
print("davazp followers:")
print(davazp_followers)

# for repo in gh.get_user().get_repos():
#     print(repo.name)
#    repo.edit(has_wiki=False)
