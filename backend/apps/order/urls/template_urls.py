from django.urls import path
from apps.order.views import template_views

app_name = "cart"
urlpatterns = [
    path("create/", template_views.CartView.as_view(), name="order_create"),
]
