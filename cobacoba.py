#Make Empty Matrix
matrix_len = 5
matrix_height = 2

my_empty_matrix = [[0 for _ in range(matrix_len)] for _ in range(matrix_height)]
for vec in my_empty_matrix:
    print(vec)