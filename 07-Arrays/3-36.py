arr = [[2, 1],
[3, 5],
[7, 4],
[2, 6]]

def convert(arr):
    arr2 = [0 for i in range(len(arr)*len(arr[0]))]
    k = 0
    for i in arr:
        for j in i:
            arr2[k] = j
            k += 1
    return arr2

print(convert(arr))