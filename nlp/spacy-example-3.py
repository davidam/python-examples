import spacy
from spacy.lang.es.examples import sentences

nlp = spacy.load("es_core_news_sm")
doc = nlp(sentences[0])
print("Document:" + doc.text)

print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
