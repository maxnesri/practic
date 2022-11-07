product = {
    "ноутбук msi": {
        "цена": 120000,
        "количество": 66,
        "категория": "техника"
    },

    "клавиатура dell": {
        "цена": 1500,
        "количество": 100,
        "категория": "техника"
    },
    
    "apple watch": {
        "цена": 35000,
        "количество": 27,
        "категория": "часы"
    },

    "наушники razer": {
        "цена": 2500,
        "количество": 156,
        "категория": "наушники"
    },
    "колонка JBL":{
        "цена": 10000,
        "количество": 120,
        "категория": "гарнитура"
    }
}  
money = int(0)
def wealth(product_dict: dict):
    for kind, box in product_dict.items():
        print("-"*70)
        print(f"Товар {kind!r}")
        print("-"*70)
        for asset, pages in box.items():
            print(f" {asset} - {pages} ")

def purchases(product_dict : dict, price : int):
    products = input("Введите название товара: ")
    for znac in product_dict.values():
        if products in znac:
            numOfProducts = input("Введите количество товара: ")
             for  in product_dict.values():
        if products in znac:
        
    print("товар отсутствует")  
   
    

    
if __name__ == '__main__':
    wealth(product)
    purchases()
