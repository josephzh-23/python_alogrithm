
import docx2txt
from docx import Document
my_text = Document("/Users/josephzh/Desktop/Array_problems.docx")

for p in my_text.paragraphs:
    if 'problem' in p.text:
        print(p.text)