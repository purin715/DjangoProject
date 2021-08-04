from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True


# Form들이 UserCreationForm을 상속받도록 변경하며,
# class 속성을 재정의하기 위해 초기화 메서드 __init__()을 오버라이드 한다.

# def __init__(self)의 괄호 안에 들어가는 변수는 무조건 정의 해줘야한다. 안해주면 에러.
# super().__init__()의 괄호 안에 정의하는 변수는 부모 클래스에서 정의해야만 하는 변수들을 넣어줘야 한다
# args는 tuple형, kwargs는 dictionary형으로 변수를 저장
# 특정 클래스를 상속할 경우, 자식 클래스에 super().__init__()을 삽입해야만 부모클래스의 변수를 상속받을 수 있다.