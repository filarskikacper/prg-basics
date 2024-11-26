arr = [2, 6, 4, 9, 7]
for num in arr:
    print(f"{num}: ", end="")
    for i in range(num): print("*", end="")
    print()
