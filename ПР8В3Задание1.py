import math

def calculate_hypotenuse(cathetus1, cathetus2):
    return math.sqrt(cathetus1**2 + cathetus2**2)

# Катеты первого треугольника
cathetus1_triangle1 = 3
cathetus2_triangle1 = 4

# Катеты второго треугольника
cathetus1_triangle2 = 5
cathetus2_triangle2 = 12

# Вычисляем гипотенузы
hypotenuse1 = calculate_hypotenuse(cathetus1_triangle1, cathetus2_triangle1)
hypotenuse2 = calculate_hypotenuse(cathetus1_triangle2, cathetus2_triangle2)

# Сравниваем и выводим результаты
if hypotenuse1 > hypotenuse2:
    print("Гипотенуза первого треугольника больше:", hypotenuse1)
    print("Гипотенуза второго треугольника меньше:", hypotenuse2)
elif hypotenuse1 < hypotenuse2:
    print("Гипотенуза первого треугольника меньше:", hypotenuse1)
    print("Гипотенуза второго треугольника больше:", hypotenuse2)
else:
    print("Гипотенузы равны:", hypotenuse1)
