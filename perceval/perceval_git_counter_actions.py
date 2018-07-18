#! /usr/bin/env python3
# Count commits
# You can execute this script following this tutorial:
# https://grimoirelab.gitbooks.io/training/perceval/first_steps.html
# source ~/venvs/perceval/bin/activate
# $ python3 ~/git/python-examples/perceval/perceval_git_counter.py https://github.com/grimoirelab/perceval.git /tmp/clonedir

import argparse
from pprint import pprint
from perceval.backends.core.git import Git

# Read command line arguments
parser = argparse.ArgumentParser(description = "Count commits in a git repo")
parser.add_argument("repo", help = "Repository url")
parser.add_argument("dir", help = "Directory for cloning the repository")
parser.add_argument("--print", action='store_true', help = "Print hashes")
args = parser.parse_args()

# create a Git object, and count commmits
repo = Git(uri=args.repo, gitpath=args.dir)
a = 0
m = 0
for commit in repo.fetch():
    for f in commit['data']['files']:
        if ('action' in f.keys()):
            if (f['action'] == 'A'):
                a += 1
            if (f['action'] == 'M'):
                m += 1

print("Number of merges: ", m)
print("Number of normal commits: ", a)
