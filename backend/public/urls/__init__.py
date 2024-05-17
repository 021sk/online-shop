from django.urls import path
from public.views import template

# app_name = 'home'
urlpatterns = [
    path("", template.HomeView.as_view(), name="home"),
]
