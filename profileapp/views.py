from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm # 어떤 폼을 입력받아서 할 것인지
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'