from document import Document

# my_text = Document("/Users/josephzh/Desktop/system_design/design_url_shortener.docx")
import docx2txt


words = ["What", "how", "what", "where", "Where", "what's", "?-"]

my_text = docx2txt.process("/Users/qzhou/Desktop/system_design/Design_url_shortener.docx")
results = my_text.split('\n')
for p in results:
    if [ele for ele in words if (p.startswith(ele))]:
        print(p)
# with open("/Users/qzhou/Desktop/system_design/Design_url_shortener.docx", 'r') as reader:
#      for line in reader:
#          print(line, end='')