from django.urls import path, include

urlpatterns = [
    path("api_cart/", include("apps.order.urls.api_urls")),
    path("cart/", include("apps.order.urls.template_urls")),
]
