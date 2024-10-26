def e(letters):
    number = 0
    for char in letters:
        if char == 'e':
            number += 1
    return number

letters = input('Input anything here: ')
print(f'The number of letter "e": {e(letters)}')