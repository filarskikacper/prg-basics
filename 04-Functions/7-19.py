def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range (2, n):
            if n % i == 0:
                return False
    return True

def f(n):
    count = 0
    number = 1
    while count < n:
        number += 1
        if isPrime(number) == True:
            count += 1
    return number
