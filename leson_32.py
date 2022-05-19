def examination(a, b):
    """Проверка деление на 0"""
    try:
        print(int(a / b))
    except ZeroDivisionError:
        print("айайай делить на 0 не нельзя")


def mistake(a, b):
    """Кастомная ошибка"""
    breakpoint()
    print(a/b)
