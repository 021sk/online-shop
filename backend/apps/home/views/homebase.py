# Create your views here.
from django.views import generic
from django.shortcuts import render, get_object_or_404

from apps.home.models import Product, Category


class HomeView(generic.TemplateView):
    template_name = "public/index.html"


class ProductListView(generic.View):
    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(
            request,
            "public/shop.html",
            {
                "products": products,
                "categories": categories,
            },
        )


class ProductDetailView(generic.View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(
            request, "public/product-detail-no-reply.html", {"product": product}
        )
