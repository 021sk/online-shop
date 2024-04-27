from django.urls import path, include
# from apps.home.views import homebase

urlpatterns = [
    path("product/", include("apps.home.urls.product")),
    path("", include("apps.home.urls.homebase")),
    # path("", homebase.HomeView.as_view(), name="home"),
]
