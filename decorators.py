def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated

@decorator
def hello_world(input_text):
    print(input_text)

hello_world('Hello World!')

def checker(func):
    def decorated(width, height):
        if width > 0 and height > 0:
            print("True")
        else:
            print("False")
        func(width, height)
    return decorated

@checker
def triangle(width, height):
    area = (width * height) / 2
    print("삼각형 면적 : ", area)

@checker
def rectangular(width, height):
    area = (width * height)
    print("사각형 면적", area)

triangle(2, 3)
rectangular(2, 3)