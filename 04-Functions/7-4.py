def isNumber(number, x, y):
    if number >= x and number <= y:
        return True
    else:
        return False

number, x, y = map(int, input('Enter number, x and y: ').split())
print(f'Number {number} in range <{x},{y}>: {isNumber(number, x, y)}')