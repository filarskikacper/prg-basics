def f(amount_to_pay):
    coins = 0
    if amount_to_pay // 5 > 0:
        coins += amount_to_pay // 5
        amount_to_pay -= (amount_to_pay // 5 * 5)
    if amount_to_pay // 2 > 0:
        coins += amount_to_pay // 2
        amount_to_pay -= (amount_to_pay // 2 * 2)
    coins += amount_to_pay
    return coins

amount_to_pay = int(input('Enter the amount in PLN: '))

print(f(amount_to_pay))