def month(n):
    if n == 1:
        return 'January'
    elif n == 2:
        return 'February'
    
date = int(input('Enter number of month: '))
print(month(date))