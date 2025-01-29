def is_symmetric(matrix):
    n = len(matrix)  # Размерность матрицы
    for i in range(n):
        for j in range(i + 1, n):  # Проверяем только верхний треугольник
            if matrix[i][j] != matrix[j][i]:  # Сравниваем элементы
                return False  # Если не равны, матрица не симметрична
    return True  # Все элементы соответствуют, матрица симметрична

# Пример использования
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
print(is_symmetric(matrix))
