
from django.urls import path
from .views import hello_world, AccountCreateView

app_name = "account"

urlpatterns = [

    path('hello_world/', hello_world, name="hello_world" ),  # 라우터에 대한 이름
    path("create/", AccountCreateView.as_view(), name="create" )
]
