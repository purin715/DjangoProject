from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm # 어떤 폼을 입력받아서 할 것인지
    template_name = 'profileapp/create.html'

    def form_valid(self, form):  # form : 클라이언트가 데이터를 넣어놓은 ProfileCreationForm
        form.instance.user = self.request.user  # 유저 특정해주기, 폼이 생성되면
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    # 클래스 자체에서는 pk값을 넘겨줄 수 없다 따라서 동적으로 넘겨줄 함수를 오버라이딩
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})