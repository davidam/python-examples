import re

print re.split(r'\W+', 'Words, words, words.')
print re.split(r'(\W+)', 'Words, words, words.')
print re.split(r'\W+', 'Words, words, words.', 1)
print re.split('x*', 'axbc')
