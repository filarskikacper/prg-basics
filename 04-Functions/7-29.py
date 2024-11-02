def f(n):
    if n < 1:
        return 'Wrong value'
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return n + f(n-1)

print(f(10))