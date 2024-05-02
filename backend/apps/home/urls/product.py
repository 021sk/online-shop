from django.urls import path
from apps.home.views import homebase

app_name = "product"
urlpatterns = [
    path("", homebase.ProductListView.as_view(), name="product-list"),
    path(
        "<slug:category_slug>",
        homebase.ProductListView.as_view(),
        name="product-list-filter",
    ),
    path("<slug:slug>/", homebase.ProductDetailView.as_view(), name="product-detail"),
    # /profile/
    # /notification
    # /(search)/product/<key>
]
