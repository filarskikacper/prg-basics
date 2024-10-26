def hide(card_number):
     if len(card_number) != 16:
          return 'Wrong card number'
     else:
        hidden_number = card_number[:2] + '**********' + card_number[12:16]
        return hidden_number

card_number = input('Enter your card number: ')
print(f'For card {card_number} function returns {hide(card_number)}')