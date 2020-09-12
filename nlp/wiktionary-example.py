
from wiktionaryparser import WiktionaryParser
parser = WiktionaryParser()
word = parser.fetch('test')
another_word = parser.fetch('test', 'french')
parser.set_default_language('french')
parser.exclude_part_of_speech('noun')
parser.include_relation('alternative forms')
print(word)
