#!/usr/bin/env python
import sys
import subprocess

if len(sys.argv) == 2:
    word = str(sys.argv[1])
    subprocess.call("dict -d fd-eng-spa " + word, shell=True)
else:
    print("You must write the word to translate")
