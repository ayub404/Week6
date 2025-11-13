matrix_4x4 = [
	[ 1,  2,  3,  4],
	[ 5,  6,  7,  8],
	[ 9, 10, 11, 12],
	[13, 14, 15, 16],
    
]
matrix_3x3 = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
def sum_diagonals(matrix):
    diogonal = 0
    ant_diogonal = 0
    
    iscenter = False
    for i in range(len(matrix)):
        diogonal += matrix[i][i]
    for i in range(len(matrix)):
        ant_diogonal += matrix[i][len(matrix) - 1 -i]
    sum = diogonal + ant_diogonal
    if len(matrix) %2 != 0:
        iscenter = True
        pre_center = matrix[len(matrix) // 2]
        center = pre_center[len(pre_center) // 2]
        
        sum = diogonal + ant_diogonal - center
    print(f"Primary diagonal: {diogonal}")
    print(f"Anti-diagonal: {ant_diogonal}")
    if iscenter:
        print(f"The center element: {center}")
    print(f"Total sum: {sum}")
    print(f"Expected output: {sum}")
result1 = sum_diagonals(matrix_4x4)
result2 = sum_diagonals(matrix_3x3)

    
    


