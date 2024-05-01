from django.urls import path
from apps.accounts import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path(
        "verification/<str:username>/<str:token>",
        views.VerificationView.as_view(),
        name="verification",
    ),
    path("register/", views.UserRegisterView.as_view(), name="registration"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # (auth)/forget-password
]
