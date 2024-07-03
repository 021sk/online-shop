from ..cart import Cart
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Order
from apps.accounts.models import Address


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        print(cart.__len__())
        return render(request, "public/checkout-cart.html", context={"cart": cart})


class ShipingView(LoginRequiredMixin, View):
    login_url = (
        "/auth/login/"  # Specify your login URL if it's different from the default
    )
    redirect_field_name = "next"  # This is the default redirect field name

    def get(self, request):
        user = request.user
        address = Address.objects.filter(user=user)

        cart = Cart(request)
        return render(
            request,
            "public/checkout-shipping.html",
            context={"cart": cart, "addresses": address},
        )


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        must_pay = order.get_total_price() - order.get_total_discount()
        print(must_pay)
        return render(
            request,
            "public/checkout-payment.html",
            {"order": order, "mustpay": must_pay},
        )
