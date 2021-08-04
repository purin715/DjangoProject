from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta: # Inner class로 사용하여 상위 클래스에게 meta data를 제공하는 것
        model = Profile # 어떤 모델을 기반으로 할 것인지
        fields = ['image', 'nickname', 'message'] # 클라이언트에게 받을 것

        # 클래스는 곧 객체이며, meta 클래스는 이러한 객체를 만드는 무언가이다