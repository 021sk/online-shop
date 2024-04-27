from django.urls import path
from apps.accounts import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login")
    # (auth)/login
    # (auth)/logout
    # (auth)/register
    # (auth)/activate/token
    # (auth)/forget-password
]
