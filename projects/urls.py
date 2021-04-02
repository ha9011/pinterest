from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from comments.views import CommentsCreateView, CommentsDeleteView
from profiles.views import ProfileCreateView, ProfileUpdateView
from projects.views import ProjectCreateView, ProjectDetailView, ProjectListView

app_name = "projects"

urlpatterns = [

    path("create/", ProjectCreateView.as_view(), name="create"),

    path("detail/<int:pk>", ProjectDetailView.as_view(), name="detail"),
    path("list/", ProjectListView.as_view(), name="list"),


]