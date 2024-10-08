import random
number = random.randint(1,6)
print(f'Dice rolled: {number}')
number = number == 1 or number == 6
print(f'Special number (1 or 6): {number}')
