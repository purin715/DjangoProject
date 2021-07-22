def checker(func):
    def checked(width, height):
        if width >= 0 and height >= 0:
            res = func(width, height)
            print(res)
        else:
            print('False')
    return checked

@checker
def triangle(width, height):
    return (width * height) / 2

@checker
def rectangular(width, height):
    return (width * height)

triangle(-2, 3)
rectangular(2, 3)