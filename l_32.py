"""1 Відрефакторити калькулятор:
    - винести усі функції в окремий файл
    - винести усі перевірки/валідації в окремий файл

2 Написати власну помилку"""
from leson_32 import examination, MycastomError
from l32 import numbers1, numbers2

# проверка на число
try:
    a = numbers1()
    try:
        b = numbers2()
        item = input("Выберите знак + , - , / , *: ")

        if item == "+":
            print(a + b)

        elif item == "-":
            print(a - b)

        elif item == "*":
            print(a * b)

        elif item == "/":
            examination(a, b)
        else:
            print("Ошибка")

    except ValueError:
        print("Вы ввели буквы а не цыфры")
except ValueError:
    print("Вы ввели буквы а не цыфры")
