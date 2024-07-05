
import docx2txt
from docx import Document
my_text = Document("/Users/josephzh/Desktop/system_design/microservice_communication.docx")


words = ["What", "how", "what", "where", "Where", "what's", "?-"]
for p in my_text.paragraphs:
    # print(p.text)
    if [ele for ele in words if(ele in p.text)]:
        print(p.text)