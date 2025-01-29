a = int(input("Введите A: "))
b = int(input("Введите B: "))
a -= ~a & 1
b += ~b & 1
for i in range (a, b - 1, -2):
 print(i)
