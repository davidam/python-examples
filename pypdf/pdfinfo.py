from PyPDF2 import PdfFileReader
p = r'one.pdf'
pdf = PdfFileReader(file(p, 'rb'))
print(pdf.documentInfo)
print(pdf.getNumPages())
info = pdf.getDocumentInfo()
print(info.author)
print(info.creator)
print(info.producer)
print(info.title)
