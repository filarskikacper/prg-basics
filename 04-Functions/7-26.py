def f(x):
    remainder = (int(x[0]) + int(x[1]) + int(x[2])) % 7
    if int(x[3]) == remainder:
        return True
    return False
print(f("1082"))