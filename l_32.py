"""1 Відрефакторити калькулятор:
    - винести усі функції в окремий файл
    - винести усі перевірки/валідації в окремий файл

2 Написати власну помилку"""
from leson_32 import examination,mistake
from l32 import numbers1,numbers2

a = numbers1()
b = numbers2()

item = input("Выберите знак + , - , / , *: ")

if item == "+":
    print(a + b)

elif item == "-":
    print(a - b)

elif item == "*":
    print(a * b)

elif item == "/":
    examination(a,b)
    #mistake(a,b) - власна помилка
