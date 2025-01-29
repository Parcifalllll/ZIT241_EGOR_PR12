import math

# Заданные значения
x = 3.74 * 10**-2
y = -0.825
z = 0.16 * 10**2

# Вычисляем части выражения
sin_squared = math.sin(x + y)**2
numerator = 1 + sin_squared
denominator = abs(x - (2 * y) / (1 + x**2 * y**2))

# Вычисляем вторую часть
cos_squared = math.cos(math.atan(1 / z))**2

# Полное вычисление s
s = (numerator / denominator) * (x**abs(y) + cos_squared)

# Вывод результата
print(f"s = {s:.5f}")  # Форматируем вывод для 5 знаков после запятой
