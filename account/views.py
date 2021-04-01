from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from account.forms import AccountUpdateForm


def hello_world(request):
    qwe = "q"
    # return HttpResponse("hello world!")
    return render(request, "account/hello_world.html")  # templates in setting 설정


class AccountCreateView(CreateView):
    model = User  # 모델 기본제공
    form_class = UserCreationForm  # 기본제공
    success_url = reverse_lazy("account:hello_world")  # 성공시 리다리엑트
    # reverse Vs reverse_lazy 차이는 함수 // 클레스 차이
    template_name = "account/create.html"  # 현재 템플릿(아이디 생성할..)


class AccountUpdateView(UpdateView):
    model = User  # 모델 기본제공
    form_class = AccountUpdateForm  # 커스텀
    context_object_name = 'target_user'
    success_url = reverse_lazy("account:hello_world")  # 성공시 리다리엑트
    # reverse Vs reverse_lazy 차이는 함수 // 클레스 차이
    template_name = "account/update.html"  # 현재 템플릿(아이디 생성할..)


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'  # model을 다르게 해야한다, 똑같이 user로 할 경우 로그인 세션의 user로 인식됨
    template_name = "account/detail.html"


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy("account:login")  # 성공시 리다리엑트
    template_name = "account/delete.html"
