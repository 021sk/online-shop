from django.shortcuts import render, get_object_or_404
from apps.home.models import Product, Category
from django.views import generic


class ProductListView(generic.View):
    template_name = "public/shop.html"

    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(
            request,
            self.template_name,
            {
                "products": products,
                "categories": categories,
            },
        )


class ProductDetailView(generic.View):
    template_name = "public/product-detail-no-reply.html"

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, self.template_name, {"product": product})
