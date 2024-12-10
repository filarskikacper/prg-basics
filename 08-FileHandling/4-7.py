import re

text = input("Enter text: ")
pattern = '[aeiou]'
vowels = re.findall(pattern, text)
print(len(vowels))
