arr = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for i in range (len(arr)):
    for j in range (len(arr[i])):
        if j == i:
            arr[i][j] = 1
        print(arr[i][j], end=' ')
    print()

