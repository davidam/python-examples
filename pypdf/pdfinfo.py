from pypdf import PdfReader

reader = PdfReader("one.pdf")

meta = reader.metadata

# All the following could be None!
print(meta.title)
print(meta.author)
print(meta.subject)
print(meta.creator)
print(meta.producer)
print(meta.creation_date)
print(meta.modification_date)
