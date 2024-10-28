def f(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True
    else:
        return False

n1, n2, n3 = map(int, input('Enter three numbers: ').split())
print(f(n1,n2,n3))