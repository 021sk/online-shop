from django.urls import path
from apps.accounts import views
# from django.views import generic


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path(
        "verification/<str:username>/<str:token>",
        views.VerificationView.as_view(),
        name="verification",
    ),
    # path(
    #     "activate",
    #     generic.TemplateView.as_view(template_name="pages/activate.html"),
    #     name="public_activate_page",
    # ),
    # (auth)/login
    # (auth)/logout
    # (auth)/register
    # (auth)/activate/token
    # (auth)/forget-password
]
