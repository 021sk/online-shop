from django.urls import path, include
from django.views import generic

urlpatterns = [
    path("auth/", include("apps.accounts.urls.auth")),
    path(
        "activate",
        generic.TemplateView.as_view(template_name="pages/activate.html"),
        name="public_activate_page",
    ),
]
