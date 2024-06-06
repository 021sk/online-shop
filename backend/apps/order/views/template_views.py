from ..cart import Cart
from django.views import View
from django.shortcuts import render


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        print(cart.__len__())
        return render(request, "public/checkout-cart.html", context={"cart": cart})
