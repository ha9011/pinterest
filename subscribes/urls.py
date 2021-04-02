from django.urls import path

from subscribes.views import SubscribesView, SubscribesListView

app_name = "subscribes"

urlpatterns = [
    path("subscribe/", SubscribesView.as_view(), name="subscribe"),
path("list/", SubscribesListView.as_view(), name="list"),
]