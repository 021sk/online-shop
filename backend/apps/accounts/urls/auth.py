from django.urls import path
from apps.accounts.views import auth
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", auth.LoginView.as_view(), name="login"),
    path(
        "verification/<str:username>/<str:token>",
        auth.VerificationView.as_view(),
        name="verification",
    ),
    path("register/", auth.UserRegisterView.as_view(), name="registration"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    path("user_edit/", auth.edit_user, name="edit_account"),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            success_url="password_change",
            template_name="public/profile-editpassword.html",
        ),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # (auth)/forget-password
]
