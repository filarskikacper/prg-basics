current_price = float(input('Enter current product price: '))
previous_price = float(input('Enter previous product price: '))
discount = int(100 - (current_price / previous_price * 100))
if discount >= 10:
    print("Buy the product!!")
    print(f'Product price reduced by {discount}%')

