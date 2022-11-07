Products = {
"Pizza": 304,
"rice": 116,
"borch": 78,
"roll" : 41
}

kall= int(0)

for eat in Products.keys():

    print(f"В блюде {eat} {Products.get(eat)} ккал")
per = int(input("Введите количество блюд: "))

pr = ""

jj = 0

while jj < per:
    pr = input("Enter name of product: ")
    if pr in Products.keys():
        print(f"{pr} здесь")
        kall = kall+ Products.get(pr)
    else:
        print(f"{pr} - такого блюда нет")
        jj+=1

print(f"Всего ккал: {kall}")
