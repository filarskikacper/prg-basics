###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    sum = 0
    number = str(abs(number))
    for char in number:
        char = int(char)
        sum += char
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')