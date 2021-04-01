from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from profiles.views import ProfileCreateView, ProfileUpdateView

app_name = "articles"

urlpatterns = [

    path("list/", TemplateView.as_view(template_name="articles/list.html"), name="list"),


]
