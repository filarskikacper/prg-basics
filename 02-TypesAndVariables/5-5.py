price = float(input('Enter price: '))
discount = float(input('Enter discount (%): '))
price_with_discount = round(((1 - discount / 100) * price), 2)
reduction = round((price - price_with_discount), 2)

print(f"Price with discount: {price_with_discount}")
print(f"Reduction: {reduction}")