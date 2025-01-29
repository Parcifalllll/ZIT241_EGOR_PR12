def read_matrix(file_name):
    with open(file_name, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file if line.strip()]
    return matrix

def write_matrix(file_name, matrix):
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def process_matrices(input_file, output_file):
    matrix = read_matrix(input_file)
    # Пример обработки: транспонирование матрицы
    transposed_matrix = [list(row) for row in zip(*matrix)]
    write_matrix(output_file, transposed_matrix)

# Задайте имена файлов
input_file_name = 'МалаховЕгорГеннадьевич_ЗИТ241_vvod.txt'
output_file_name = 'МалаховЕгорГеннадьевич_ЗИТ241_vivod.txt'

write_matrix(output_file_name, result)
