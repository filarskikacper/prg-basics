arr = [[-38, 19], [5,40],[-7,11],[29,16]]

def swap2d(arr):
    temp = arr[0]
    arr[0]=arr[len(arr)-1]
    arr[len(arr)-1] = temp
    return arr

print(arr)
print(swap2d(arr))

