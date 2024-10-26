def f(number, even):
    sum = 0
    if even is True:
        for char in number:
            if int(char) % 2 == 0:
                sum += int(char)
    else:
        for char in number:
            if int(char) % 2 != 0:
                sum += int(char)
    return sum

number = input('Enter number: ')
even = input('Is your sum even? (y/n): ')
if even == 'y':
    even = True
else: even = False
print(f(number, even))