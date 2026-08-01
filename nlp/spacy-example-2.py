## python -m spacy download es_core_news_sm

import spacy
nlp = spacy.load("es_core_news_sm")
import es_core_news_sm
nlp = es_core_news_sm.load()
doc = nlp("Esto es una frase.")
print([(w.text, w.pos_) for w in doc])
