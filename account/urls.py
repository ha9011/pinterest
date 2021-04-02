from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import  AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "account"

urlpatterns = [


    path("login/", LoginView.as_view(template_name="account/login.html"), name="login" ),   # 로그인 하고 리다이렉트할 템플릿
    path("logout/", LogoutView.as_view(), name="logout" ),
    path("create/", AccountCreateView.as_view(), name="create" ), # 계정 생성
    path("update/<int:pk>", AccountUpdateView.as_view(), name="update" ), # 계정 수정
    path("detail/<int:pk>", AccountDetailView.as_view(), name="detail") , # 계정 정보
    path("delete/<int:pk>", AccountDeleteView.as_view(), name="delete")  # 계정 삭제
]
