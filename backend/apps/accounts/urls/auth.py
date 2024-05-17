from django.urls import path
from apps.accounts.views import auth

urlpatterns = [
    path("login/", auth.LoginView.as_view(), name="login"),
    path(
        "verification/<str:username>/<str:token>",
        auth.VerificationView.as_view(),
        name="verification",
    ),
    path("register/", auth.UserRegisterView.as_view(), name="registration"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    # (auth)/forget-password
]
