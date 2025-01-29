def rearrange_matrix(matrix):
    # Находим максимальный элемент и его индексы
    max_value = -float('inf')
    max_row = max_col = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_row, max_col = i, j

    # Переставляем строки
    if max_row != 0:
        matrix[0], matrix[max_row] = matrix[max_row], matrix[0]

    # Переставляем столбцы
    for i in range(len(matrix)):
        if max_col != 0:
            matrix[i][0], matrix[i][max_col] = matrix[i][max_col], matrix[i][0]

    return matrix

# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = rearrange_matrix(matrix)
for row in result:
    print(row)
