import PyPDF2

path = open('one.pdf', 'rb')
path2 = open('two.pdf', 'rb')

merger = PyPDF2.PdfFileMerger()

merger.merge(position=0, fileobj=path2)
merger.merge(position=2, fileobj=path)
merger.write(open("res.pdf", 'wb'))
