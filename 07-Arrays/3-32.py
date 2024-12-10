arr = [[-38, 19], [5,40],[-7,11],[29,16]]

def swap2d(arr):
    for i in arr:
        for j in i:
            temp = j
            j+1 = temp

print(arr)
print(swap2d(arr))

