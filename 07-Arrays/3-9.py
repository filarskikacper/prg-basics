arr1 = ["water","book","sky"]
arr2 = ["water","book","sky"]

def f(arr1, arr2):
    if len(arr1) != len(arr2):
        return "arrays are different length"
    else:
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return f"{arr1[i]} is different from {arr2[i]}"
    return "arrays are the same"
            
print("Array1: ", arr1)
print("Array1: ", arr2)
print("Comparison", f(arr1,arr2))