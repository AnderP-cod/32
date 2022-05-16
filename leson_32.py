def examination(a,b):
    try:
        print(int(a / b))
    except ZeroDivisionError:
        print("айайай делить на 0 не нельзя")

def mistake(a,b):
    breakpoint()
    print(a/b)