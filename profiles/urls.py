from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from profiles.views import ProfileCreateView

app_name = "profiles"

urlpatterns = [

    path("create/", ProfileCreateView.as_view(), name="create")

]
