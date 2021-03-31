from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView


def hello_world(request):
    qwe = "q"
    #return HttpResponse("hello world!")
    return render(request, "account/hello_world.html")  # templates in setting 설정


class AccountCreateView(CreateView):
        model = User   # 모델 기본제공
        form_class = UserCreationForm # 기본제공
        success_url = reverse_lazy("account:hello_world")  # 성공시 리다리엑트
        # reverse Vs reverse_lazy 차이는 함수 // 클레스 차이
        template_name = "account/create.html"  # 현재 템플릿(아이디 생성할..)
