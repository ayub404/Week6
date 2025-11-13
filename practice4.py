matrix_3x2 = [
	[1, 2],
	[3, 4],
	[5, 6]
]

matrix_2x2 = [
	['a', 'b'],
	['c', 'd']
]


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_row = []
    for j in range(cols):
        new_cols = []
        for i in range(rows):
            new_cols.append(matrix[i][j])
        new_row.append(new_cols)
    return new_row


print(transpose_matrix(matrix_3x2))

print(transpose_matrix(matrix_2x2))