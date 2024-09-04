from PyPDF2 import PdfReader

reader=PdfReader("Brief overview and on requirement.pdf")
numpage=len(reader.pages)
page=reader.pages[0]
txt=page.extract_text()
print(txt)