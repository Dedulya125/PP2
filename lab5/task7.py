import re

def snakeToCamel(text):
    camelCase=""
    pattern = re.compile(r"[_]")
    words=pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            camelCase+=word.capitalize()
        else: 
            camelCase += word
    return camelCase

row_text = r"C:\Users\Nurbek\Desktop\pp2\lab5\row.txt"

with open(row_text, 'r', encoding='utf-8') as file:
    text = file.read()

print(snakeToCamel(text))