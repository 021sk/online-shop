from django.urls import path
from apps.order.views import api_views

app_name = "api_cart"
urlpatterns = [
    path(
        "add/<int:product_id>", api_views.CartAddApiView.as_view(), name="add_to_cart"
    ),
    path(
        "update_quantity/",
        api_views.UpdateQuantityView.as_view(),
        name="update_quantity",
    ),
    path("remove_item/", api_views.RemoveItemView.as_view(), name="remove_item"),
    path("order-create/", api_views.OrderCreateView.as_view(), name="order_create"),
    path(
        "active_address/<int:address_id>",
        api_views.ActiveAddressView.as_view(),
        name="active_address",
    ),
]
