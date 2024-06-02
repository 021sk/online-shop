from django.urls import path
from apps.order.views import api_views

app_name = "api_cart"
urlpatterns = [
    path(
        "add/<int:product_id>", api_views.CartAddApiView.as_view(), name="add_to_cart"
    ),
]
