import re

with open('email.txt', 'r') as file:
    content = file.read()

pattern1 = '^From:.*<([^>]+)>'
sender_email = re.findall(pattern1, content, re.MULTILINE)
print(sender_email)