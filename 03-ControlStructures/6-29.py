def isPrime(n):
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

number = 1

n = int(input('Enter number: '))

while n > 0:
    number += 1
    if isPrime(number):
        print(number, end=' ')
        n -= 1