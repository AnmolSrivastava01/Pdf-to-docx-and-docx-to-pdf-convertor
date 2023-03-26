from pdf2docx import Converter

old_pdf="C:/Users/admin/Desktop/python projects/project 8/Untitled document.pdf"
new_doc="C:/Users/admin/Desktop/python projects/project 8/new.docx"
o=Converter(old_pdf)
o.convert(new_doc)
o.close()
#for doc to pdf
from docx2pdf import convert

convert("C:/Users/admin/Desktop/python projects/project 8/new.docx","C:/Users/admin/Desktop/python projects/project 8/oops.pdf")
