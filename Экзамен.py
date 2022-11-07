questions = dict()

def show_questions():
    print("Список активных задач:")
    for name in questions.keys():
        print(name)

def details():
    name = input("Введите имя задачи: ")
    description = questions.get(name, "Задача не найдена")
    print(description)

def add_questions():
    print("Добавление новой задачи")
    name = input("Введите имя задачи: ")
    description = input("Введите описание: ")
    questions[name] = description
    print("Задача успешно добавлена")

def del_questions():
    print("Удаление задачи")
    name = input("Введите имя задачи: ")
    if name in questions:
        del questions[name]
        print(f"Задача {name} удалена")
    else:
        print("Задача не найдена")

if __name__ == '__main__':
    while True:
        msg = """
[1] Вывести список задач
[2] Посмотреть подробности задачи
[3] Добавить задачу
[4] Удалить задачу
[5] Выход
Пожалуйста, введите соответствующую цифру: """
        num = int(input(msg))
        if num == 1:
            show_questions()
        elif num == 2:
            details()
        elif num == 3:
            add_questions()
        elif num == 4:
            del_questions()
        elif num == 5:
            print("До свидания")
            break
        else:
            print("Введена неверная цифра")
