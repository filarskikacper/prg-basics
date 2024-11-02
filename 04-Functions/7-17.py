def f(sentence):
    sentence2 = ''
    for char in sentence:
        if char != ' ':
            sentence2 += char
    return sentence2

sentence = input('Enter sentence: ')
print(f(sentence))