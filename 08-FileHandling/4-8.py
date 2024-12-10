import re

with open('files.txt', 'r') as file:
    content = file.read()
    lines = content.splitlines()
    pattern = '.*.html$'
    for line in lines:
        if re.findall(pattern, line) != []:
            print(re.findall(pattern, line))