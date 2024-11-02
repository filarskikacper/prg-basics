def f(text):
    text1 = ''
    for i, char in enumerate(text):
        if i+1 < len(text):
            text1 += char + '-'
        else: text1 += char
    return text1
print(f(""))