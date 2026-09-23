import random
import spacy
from spacy.tokens import Span
from spacy.tokens import DocBin


nlp = spacy.blank("en")

# Create a Doc with entity spans
doc1 = nlp("iPhone X is coming")
doc1.ents = [Span(doc1, 0, 2, label="GADGET")]
# Create another doc without entity spans
doc2 = nlp("I need a new phone! Any tips?")

docs = [doc1, doc2]

#print(docs)

random.shuffle(docs)
train_docs = docs[:len(docs) // 2]
print(train_docs)
dev_docs = docs[len(docs) // 2:]
print(dev_docs)

# Create and save a collection of training docs
train_docbin = DocBin(docs=train_docs)
train_docbin.to_disk("./train.spacy")
# Create and save a collection of evaluation docs
dev_docbin = DocBin(docs=dev_docs)
dev_docbin.to_disk("./dev.spacy")
