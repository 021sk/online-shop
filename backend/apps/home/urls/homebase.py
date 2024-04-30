from django.urls import path
from apps.home.views import homebase

# app_name = 'home'
urlpatterns = [
    path("", homebase.HomeView.as_view(), name="home"),
]
