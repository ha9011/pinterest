from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, reverse

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from account.decorators import account_ownsership_required
from account.forms import AccountUpdateForm

has_ownership = [account_ownsership_required, login_required]


@login_required
def hello_world(request):
    qwe = "q"
    # return HttpResponse("hello world!")
    if request.user.is_authenticated:

        return render(request, "account/hello_world.html")  # templates in setting 설정

    else:
        return HttpResponseRedirect(reverse("account:login"))  # templates in setting 설정


class AccountCreateView(CreateView):
    model = User  # 모델 기본제공
    form_class = UserCreationForm  # 기본제공
    success_url = reverse_lazy("account:hello_world")  # 성공시 리다리엑트
    # reverse Vs reverse_lazy 차이는 함수 // 클레스 차이
    template_name = "account/create.html"  # 현재 템플릿(아이디 생성할..)


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'  # model을 다르게 해야한다, 똑같이 user로 할 경우 로그인 세션의 user로 인식됨
    template_name = "account/detail.html"

    def get(self, *args, **kwargs):  # method get
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()  #

    def post(self, *args, **kwargs):  # method get
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()  #


@method_decorator(has_ownership, "get")  # 일반 메소드에서 사용하는 데코를 클레스에서도 쓰게 하는 데코
@method_decorator(has_ownership, "post")  # 일반 메소드에서 사용하는 데코를 클레스에서도 쓰게 하는 데코
class AccountUpdateView(UpdateView):
    model = User  # 모델 기본제공
    form_class = AccountUpdateForm  # 커스텀
    context_object_name = 'target_user'
    success_url = reverse_lazy("account:hello_world")  # 성공시 리다리엑트
    # reverse Vs reverse_lazy 차이는 함수 // 클레스 차이
    template_name = "account/update.html"  # 현재 템플릿(아이디 생성할..)


@method_decorator(has_ownership, "get")  # 일반 메소드에서 사용하는 데코를 클레스에서도 쓰게 하는 데코
@method_decorator(has_ownership, "post")  # 일반 메소드에서 사용하는 데코를 클레스에서도 쓰게 하는 데코
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy("account:login")  # 성공시 리다리엑트
    template_name = "account/delete.html"

    def get(self, *args, **kwargs):  # method get
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()  #

    def post(self, *args, **kwargs):  # method get
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()  #
