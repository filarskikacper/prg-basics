amount = float(input('Amount: '))
VAT = 0.23 * amount
amount = round(amount, 2)
VAT = round(VAT, 2)
print(f"Amount: {amount}, VAT: {VAT}")