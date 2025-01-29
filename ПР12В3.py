def print_odd_indexed_numbers():
    num = int(input())
    if num == 0:
        return
    if print_odd_indexed_numbers.counter % 2 == 0:  # 0, 2, 4 соответствует 1, 3, 5
        print(num)
    print_odd_indexed_numbers.counter += 1  # Увеличиваем счетчик
    print_odd_indexed_numbers()  # Рекурсивный вызов

# Инициализация счетчика
print_odd_indexed_numbers.counter = 0

# Основная программа
print_odd_indexed_numbers()
