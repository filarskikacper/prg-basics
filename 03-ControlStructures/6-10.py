age = int(input('Enter the dogs age in human years: '))
dog_age = 0
if age <= 2:
    dog_age = age * 10.5
else:
    dog_age = 2 * 10.5 + (age - 2) * 4

print(f'The dogs age in dogs years is {dog_age} years.')