
# extract text from pdfs
import re
from pdfminer.high_level import extract_pages,extract_text
'''

for page_layout in extract_pages('sample.pdf'):
    for element in page_layout:
        print(element)

'''

text = extract_text("filename.pdf")
#print(text)

#pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
pattern = re.compile(r"[a-zA-Z]+")
matches = pattern.findall(text)
#print(matches)

#for i in matches:
   # print(i)

names = [n[:-2]for n in matches]
print(names)




