#1
year = int(input("Enter year: "))

def drob(year: int) -> (bool):
    if year% 400 == 0:
        print("Visokosny")
        return True
    elif year% 100 == 0:
        print("Ne Visokosny")
        return False
    if year% 4 == 0:
        print("Visokosny")
        return True
drob(year)

#2
year = int(input("Enter year: "))

def kol_dney(year: int) -> (bool, int):
    if drob(year) == True:
        print("366 days")
        return True, 366
    else:
        print("365 days")
        return False, 365
kol_dney(year)

#3
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

def exist(day, month, year) -> (bool):
    if day <= 0 or month <= 0 or year <= 0:
        return False
    elif day < 32 and month < 13 and year > 0:
        return True
    else:
        return False
print(exist(day, month, year))

#4
string1 = input("Enter first date: ")
string2 = input("Enter second date: ")
x1, y1, z1 = string1.split('.')
x2, y2, z2 = string2.split('.')
x1, y1, z1, x2, y2, z2 = int(x1), int(y1), int(z1), int(x2), int(y2), int(z2)

def calculation(x1, y1, z1, x2, y2, z2):
    if exist(day, month, year) == True:
        dday = x1 - x2
        mmonth = y1 - y2
        yyear = z1 - z2
        print(f"{dday}.{mmonth}.{yyear}")
    else:
        print("Error")
calculation(x1, y1, z1, x2, y2, z2)

def calculation1(x1, x2):
    if exist(day, month, year) == True:
        dday = x1 - x2
        print(f"{dday}.", end="")
    else:
        print("Error")
calculation1(x1, x2)
calculation1(y1, y2)
calculation1(z1, z2)
