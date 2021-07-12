from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    # 라우팅 해줘야 해 (연결)
    # 메인 앱에서 먼저 받고 여기로 보냄
    if request.method == "POST":

        temp = request.POST.get('input')
        new_data = HelloWorld()
        new_data.text = temp
        new_data.save() # 실제 DB에 저장

        return HttpResponseRedirect(reverse('acccountapp:hello_world')) # 실제 url 주소를 역치환해준다

        # data_list = HelloWorld.objects.all() # HelloWorld의 객체들을 가져온다
        #
        # return render(request, 'accountapp/hello_world.html', context={'data_list' : data_list})
    else:
        data_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'data_list' : data_list})