
#1.0
string = input('Вводим координаты: ')
x1, y1, x2, y2 = string.split()
x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

def dist(x1, y1, x2, y2):
    return((y1 - x1)**2 + (y2 - x2)**2)**0.5
print(f'Расстояние между точками: {dist(x1, y1, x2, y2)}')

#1.1
string = input('Вводим координаты: ')
x1, y1, x2, y2, x3, y3 = string.split()
x1, y1, x2, y2, x3, y3 = float(x1), float(y1), float(x2), float(y2), float(x3), float(y3)
dist1 = []
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    first = distance(x1, y1, x2, y2)
    second = distance(x2, y2, x3, y3)
    therd = distance(x3, y3, x1, y1)
dist1.append(distance(x1, y1, x2, y2))
dist1.append(distance(x2, y2, x3, y3))
dist1.append(distance(x3, y3, x1, y1))
print(dist1)

#1.2

def square (first, second, therd):
    p = (first + second + therd) / 2
    return (p * (p - first)(p - second)(p - therd))**0.5
    print(f"Площадь треугольника: {square (first, second, therd)}")

#1.3
numbers = [
]
i = 1
while i < 6:
    line = input("Введите три числа: ")
    x, y, z = line.split()
    x, y, z = float(x), float(y), float(z)
    numbers.append([line])
    i = i + 1
print(numbers)
