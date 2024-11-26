arr = [15, 8, 31, 47, 2, 19]
x = 0
i = len(arr)
while i > 0:
    x += arr[i-1]
    i -= 1

print(x/2)