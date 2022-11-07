Products = {
    "сладкое": {
        "печеньки": 55,
        "конфеты": 66,
        "шоколад": 90,
        "торт": 600
    },

    "солёное": {
        "чипсы": 325,
        "малосольные огурчики": 100,
        "крекеры": 35,
        "морская капуста": 13
    },

    "салаты": {
        "цезарь": 150,
        "греческий": 156,
        "олевье":200
    },
    "супы":{
        "борщ": 150,
        "суп-лапша": 120,
        "щи": 135,
        "рассольник": 140,
        "том-ям":160
    }
}   
for kategory, ii in Products.items():
    print("-"*70)
    print(f"Категория: {kategory!r}")
    print("-"*70)
    for food_name, call in ii.items():
        print(f"В блюде {food_name} - {call} ккал")

food = input("Введите название блюда: ")
def here()-> (bool):
    for znach in Products:
        if food in Products[znach]:
            return True
    return False
print(here())

def kass():
    for znach in Products:
        if food in Products[znach]:
            return znach
print(kass())
