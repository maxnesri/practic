Products = ["pizza", "shawarma", "sushi", "burger", "pelmeni"]
products_count = len(Products)

product_ext = int(input("Какой продукт вы хотите заменить:"))
product_ext = product_ext - 1
if product_ext > len(Products):
    print("Ошибка - выход за пределы массива!")
    new_prodykt = input("Введите имя нового продукта:")
    Products.append(new_prodykt)
    print(f"{new_prodykt} был добавлен в список")
else:
    extange = input("На что вы хотите изменить данный продукт:")
    print(f"Вы заменили {Products[product_ext]} на {extange}")
Products[product_ext] = extange
print(f"В моём списке любимых продуктов {len(Products)}:")
i = 0
while i < len(Products):
    print(f"Я люблю есть {Products[i]}")
    i += 1
