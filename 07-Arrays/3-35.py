matrix = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

def transpose_matrix(m):
    m2 = [[0 for i in range(len(m[i]))] for i in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[i])):
            m2[i][j] = m[j][i]
    return m2

print(transpose_matrix(matrix))