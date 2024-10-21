dec_number = int(input('Enter decimal number: '))
bin_number = ''
while dec_number // 2 != 0:
    if dec_number % 2 == 0:
        bin_number += '0'
        dec_number //= 2
    elif dec_number % 2 == 1:
        bin_number += '1'
        dec_number //= 2
bin_number += '1'
bin_number = bin_number [::-1]

print(bin_number)