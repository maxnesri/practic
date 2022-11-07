product = {
    "ноутбук msi": {
        "price": 120000,
        "amount": 66,
        "kind": "техника"
    },

    "клавиатура dell": {
        "price": 1500,
        "amount": 100,
        "kind": "техника"
    },
    
    "apple watch": {
        "price": 35000,
        "amount": 27,
        "kind": "часы"
    },

    "наушники razer": {
        "price": 2500,
        "amount": 156,
        "kind": "наушники"
    },
    "колонка JBL":{
        "price": 10000,
        "amount": 120,
        "kind": "гарнитура"
    }
}  

money = 0 
def add_money(amount: int):
     global money
     money += amount
     
def buy(product: str, goods_dict: dict):
    if product not in goods_dict:
        return False
    if goods_dict[product].get("amount", 0) <= 0:
        return False
    goods_dict[product]["amount"] -= 1
    add_money(goods_dict[product]["price"])
    return True
    
def test2():
    print(buy("apple watch", goods))
    print(buy("Computer", goods))
    print(money)
    
    
if __name__ == '__main__':
    test2()
