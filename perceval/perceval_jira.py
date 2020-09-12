#! /usr/bin/env python3

from datetime import datetime, timedelta
from perceval.backends.core.gerrit import Gerrit
from perceval.backends.core.jira import Jira

# hostname 
hostname = 'https://tickets.puppetlabs.com'
# retrieve only reviews changed since one day ago
from_date = datetime.now() - timedelta(days=1)

repo = Jira(hostname)


# fetch all reviews as an iterator, and iterate it printing each review id
for review in repo.fetch(from_date=from_date):
    print(review)

    
