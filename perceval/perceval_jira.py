#! /usr/bin/env python3
# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@libresoft>
# Maintainer: David Arroyo Menéndez <davidam@libresoft>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with python-examples; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
# Boston, MA 02110-1301 USA,

from datetime import datetime, timedelta
from perceval.backends.core.gerrit import Gerrit
from perceval.backends.core.jira import Jira
from pprint import pprint
# hostname 
hostname = 'https://tickets.puppetlabs.com'
# retrieve only reviews changed since one day ago
from_date = datetime.now() - timedelta(days=1)

repo = Jira(hostname)


# # fetch all reviews as an iterator, and iterate it printing each review id

for review in repo.fetch(from_date=from_date):
    print(review)
print("---------------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------------------")
for review in repo.fetch(from_date=from_date):
    pprint(review['data']['fields']['creator']['displayName'])

print("---------------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------------------")    
    
