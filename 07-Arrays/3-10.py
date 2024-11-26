arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

for num1 in arr1:
    flag = 1
    for num2 in arr2:
        if num1 == num2:
            flag = 0
            break
    if flag == 1:
        print(num1)