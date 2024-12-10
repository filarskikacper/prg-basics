arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

x = 1
for i in range(len(arr)):
    for j in range (len(arr[i])):
        arr[i][j] = x
        x +=1

print(arr)