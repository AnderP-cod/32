def examination(a,b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("айайай делить на 0 не нельзя")

def mistake(a,b):
    breakpoint()
    print(a/b)