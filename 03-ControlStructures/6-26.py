attempts = 0
pin = '0805'
while attempts < 3:
    entered_pin = input('Enter the PIN code: ')
    if entered_pin == pin:
        print('Your PIN is correct!')
        quit()
    else:
        print('Incorrect...')
        attempts += 1
print('Sorry, your payment card has been blocked.')