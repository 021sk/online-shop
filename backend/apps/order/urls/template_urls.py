from django.urls import path
from apps.order.views import template_views

app_name = "cart"
urlpatterns = [
    path("create/", template_views.CartView.as_view(), name="order_create"),
    path("shiping/", template_views.ShipingView.as_view(), name="shiping_template"),
    path(
        "detail/<int:order_id>",
        template_views.OrderDetailView.as_view(),
        name="detail_template",
    ),
]
