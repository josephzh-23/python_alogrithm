from document import Document

# my_text = Document("/Users/josephzh/Desktop/mobile system design.docx")
import docx2txt


'''
Between = means reading between the data here 
'''

words = ["What", "how", "what", "where", "Where", "what's", "?-", "How", "section", "Section", "vs", "Why", "?",
         "data schema", "scenario", "problem", "flow"]

my_text = docx2txt.process("/Users/qzhou/Desktop/system design/Study cases/Braintree docs.docx")
results = my_text.split('\n')
for p in results:
    if [ele for ele in words if (p.lower().startswith(ele.lower()))]:
        print(p)
# with open("/Users/qzhou/Desktop/system_design/Design_url_shortener.docx", 'r') as reader:
#      for line in reader:
#          print(line, end='')