products = int(input('Enter number of products purchased: '))
price = float(input('Enter product price: '))
total_price = 0
if products > 2:
    total_price = 2 * price + (products - 2) * 0.75 * price
    print(f'Amount to pay: {total_price}')
elif products > 0:
    print(f'Amount to pay {products * price}')