def f(binary_number):
    for char in binary_number:
        if char != '0' and char != '1':
            return False
    return True

binary_number = input('Enter binary number: ')
print(f'Is {binary_number} binary: {f(binary_number)}')