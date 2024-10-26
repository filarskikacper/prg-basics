def f(x, y):
    sum = 0
    for i in range (x, y):
        if i < 0 and i % 2 == 0:
            sum += 1
    return sum
x, y = map(int, input('Enter x, y: ').split())
print(f(x,y))