# Вводим количество минут n
n = int(input("Введите количество минут: "))

# Вычисляем количество часов и минут
total_minutes_in_a_day = 1440  # 24 часа * 60 минут
n = n % total_minutes_in_a_day   # Учитываем минуты больше суток

hours = n // 60                  # Количество полных часов
minutes = n % 60                 # Оставшиеся минуты

# Выводим результат
print(hours, minutes)
