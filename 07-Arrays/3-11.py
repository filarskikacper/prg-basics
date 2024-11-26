arr1 = [15, -5, 5, 4, -10]
arr2 = [20, 3, 16, 5]
arr3 = [2, 4, 3, 6]

def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array

print(bubblesort(arr1))
print(bubblesort(arr2))
print(bubblesort(arr3))