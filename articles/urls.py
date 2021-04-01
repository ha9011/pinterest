from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from articles.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView
from profiles.views import ProfileCreateView, ProfileUpdateView

app_name = "articles"

urlpatterns = [

    path("list/", TemplateView.as_view(template_name="articles/list.html"), name="list"),
    path("create/", ArticleCreateView.as_view(), name="create"),
    path("detail/<int:pk>", ArticleDetailView.as_view(), name="detail"),
    path("update/<int:pk>", ArticleUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", ArticleDeleteView.as_view(), name="delete"),




]
