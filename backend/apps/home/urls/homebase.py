from django.urls import path
from apps.home.views import homebase

urlpatterns = [
    path("", homebase.HomeView.as_view(), name="home"),
]
