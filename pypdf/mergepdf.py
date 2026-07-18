from pypdf import PdfWriter

merger = PdfWriter()

l1 = ['one.pdf', 'two.pdf']

for pdf in l1:
    merger.append(pdf)

merger.write("res.pdf")
