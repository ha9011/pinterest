from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from comments.views import CommentsCreateView, CommentsDeleteView
from profiles.views import ProfileCreateView, ProfileUpdateView

app_name = "comments"

urlpatterns = [

    path("create/", CommentsCreateView.as_view(), name="create"),
    path("delete/<int:pk>", CommentsDeleteView.as_view(), name="delete"),


]