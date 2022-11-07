#1
firlist = ["Borsh", "Shi", "Lapsha"]
seclist = ["Juice", "Tea", "Coffi"]

us_list = firlist + seclist
print(us_list)

number = int(input("Enter number elemment: "))
print(f"{us_list [0:number] = }")

if number % 2 == 0:
    drob = number / 2
    print(f"{us_list [0:int(drob)]}")
    print(f"{us_list [int(drob):number]}")
#2
dish = input("Enter name of dish: ")
if dish in us_list:
    us_list.remove(dish)
    print (us_list)
else:
    print("ERROR")

#3
num = int(input("Enter number: "))
liner = input("Enter line: ")

print((liner + " ") * num)
for i in range(num):
    print(liner)
