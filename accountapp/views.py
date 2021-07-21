from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld


def hello_world(request):
    # 라우팅 해줘야 해 (연결)
    # 메인 앱에서 먼저 받고 여기로 보냄

    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('input')

            new_data = HelloWorld()
            new_data.text = temp
            new_data.save() # 실제 DB에 저장

            return HttpResponseRedirect(reverse('accountapp:hello_world')) # 실제 url 주소를 역치환해준다

            # data_list = HelloWorld.objects.all() # HelloWorld의 객체들을 가져온다
            # return render(request, 'accountapp/hello_world.html', context={'data_list' : data_list})
        else:
            data_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html', context={'data_list' : data_list})

    else:
        return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' # html에서 객체를 불러오기 위해
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user: # pk로 가져온 유저 객체인지 확인
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()