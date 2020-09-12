#! /usr/bin/env python3

from datetime import datetime, timedelta
from perceval.backends.core.launchpad import Launchpad

# name 
name = "ubuntu"
# retrieve only reviews changed since one day ago
from_date = datetime.now() - timedelta(days=1)

repo = Launchpad(name)


# fetch all reviews as an iterator, and iterate it printing each review id
for review in repo.fetch(from_date=from_date):
    print(review)

    
