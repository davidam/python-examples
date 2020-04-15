
from hyphen import Hyphenator
# Create some hyphenators
h_de = Hyphenator('de_DE')
h_en = Hyphenator('en_US')
h_es = Hyphenator('es_ES')

# Now hyphenate some words
# Note: the following examples are written in Python 3.x syntax.
# If you use Python 2.x, you must add the 'u' prefixes as Hyphenator methods expect unicode strings.

print(h_en.pairs('beautiful'))
#, [['beau', 'tiful'], [u'beauti', 'ful']])

print(h_en.wrap('beautiful', 6))
#['beau-', 'tiful']

print(h_en.wrap('beautiful', 7))
#['beauti-', 'ful']

print(h_en.syllables('beautiful'))
#['beau', 'ti', 'ful']

from textwrap2 import fill
print(fill('very long text...', width=40, use_hyphenator=h_en))


