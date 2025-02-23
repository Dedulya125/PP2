import re

def spaces(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += " " + word
        else:
            res += word
    return res  

row_text = r"C:\Users\Nurbek\Desktop\pp2\lab5\row.txt"

with open(row_text, 'r', encoding='utf-8') as file:
    text = file.read()

print(spaces(text))