import re

txt = r"ab*"

pattern = re.compile(txt)

row_text = r"C:\Users\Nurbek\Desktop\pp2\lab5\row.txt"

with open(row_text, 'r', encoding='utf-8') as file:
    text = file.read()

print(pattern.search(text))