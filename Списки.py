numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2= []
new = []
n=0
for i in range(len(numbers)):
    numbers2.append(numbers[i]*5)
    print(numbers2)

for i in numbers:
    if i in numbers2:
        new.append(i)
        print(new)

for i in new:
    n += i
    print(n)

n = int(input("Введите диапазон от 1 до n: "))
numbers = [0, 1]

for i in range(n):
    numbers.append(numbers[i]+numbers[i+1])
    print(numbers)

numb = [1]
for i in range(n):
    for i in numb:
        print(numb)
