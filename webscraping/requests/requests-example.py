#! python3
#  Opens several Google search results.
import requests, sys

print('Googling...') # display text while downloading the Google page
if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
    res = requests.get('http://google.com/search?q=' + search )
    print(res.text)
else:
    print("Usted debe meter algún argumento")
