arr = [[-38, 19], 
       [5,40],
       [-7,11],
       [29,16]]

max = 0
min = 0
row_max = 0
column_max = 0
row_min = 0
column_min = 0

for i in arr:
    for j in i:
        if j > max:
            max = j
            row_max = len(i)
            column_max = len(arr)

print(max, row_max, column_max)
