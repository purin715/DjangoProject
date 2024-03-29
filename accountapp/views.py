from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld
from articleapp.models import Article


# @login_required()
# def hello_world(request):
#     # 라우팅 해줘야 해 (연결)
#     # 메인 앱에서 먼저 받고 여기로 보냄
#     if request.method == "POST":
#
#         temp = request.POST.get('input')
#
#         new_data = HelloWorld()
#         new_data.text = temp
#         new_data.save() # 실제 DB에 저장
#
#         return HttpResponseRedirect(reverse('articleapp:list')) # 실제 url 주소를 역치환해준다
#
#         # data_list = HelloWorld.objects.all() # HelloWorld의 객체들을 가져온다
#         # return render(request, 'accountapp/hello_world.html', context={'data_list' : data_list})
#     else:
#         data_list = HelloWorld.objects.all()
#         return render(request, 'accountapp/hello_world.html', context={'data_list' : data_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accountapp/create.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user' # html에서 객체를 불러오기 위해
    template_name = 'accountapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list,
                                        **kwargs)

has_ownership = [login_required, account_ownership_required]

# login이 돼있는지 여부만 판단하여 html을 보여준다
# login한 유저가 request의 유저와 같은지 여부를 판단하여 html을 보여준다
@method_decorator(has_ownership, 'get') # get방식 http에 적용해주겠다
@method_decorator(has_ownership, 'post') # post방식 http에 적용해주겠다
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})
        # target이 accountapp이므로 그냥 object.pk

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/delete.html'