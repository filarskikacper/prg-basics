number = input('Enter EAN-13 article number: ')
if len(number) == 13:
    print("Article number is correct")
    if number[0:3] == '590':
        print("Article manufactured in Poland ")