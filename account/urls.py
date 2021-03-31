from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import hello_world, AccountCreateView, AccountDetailView

app_name = "account"

urlpatterns = [

    path('hello_world/', hello_world, name="hello_world" ),  # 라우터에 대한 이름

    path("login/", LoginView.as_view(template_name="account/login.html"), name="login" ),   # 로그인 하고 리다이렉트할 템플릿
    path("logout/", LogoutView.as_view(), name="logout" ),
    path("create/", AccountCreateView.as_view(), name="create" ), # 계정 생성
    path("detail/<int:pk>", AccountDetailView.as_view(), name="detail")  # 계정 정보
]
