money = int(input('Enter the amount in PLN: '))
five_pln = 0
two_pln = 0
one_pln = 0
money_previous = money
if money // 5 > 0:
    five_pln += money // 5
    money -= (money // 5 * 5)
if money // 2 > 0:
    two_pln += money // 2
    money -= (money // 2 * 2)
one_pln = money
print(f'The amount of PLN {money_previous} in coins:')
print(f'5 PLN coins: {five_pln}')
print(f'2 PLN coins: {two_pln}')
print(f'1 PLN coins: {one_pln}')