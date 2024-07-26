from rest_framework.views import APIView
from rest_framework.response import Response
from ..cart import Cart
from django.shortcuts import get_object_or_404
from apps.home.models import Product
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.accounts.models import Address
from ..models import Order, OrderItem, Coupon
from ..serializer import CouponApplySerializer


class CartAddApiView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        try:
            cart = Cart(request)
            product = get_object_or_404(Product, id=product_id)
            cart.add(product)

            context = {
                "item_count": cart.__len__(),
                "total_price": float(
                    cart.get_total_price()
                ),  # Ensure total price is a float
            }
            return Response(context, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateQuantityView(APIView):
    def post(self, request):
        item_id = request.data.get("item_id")
        action = request.data.get("action")
        product = get_object_or_404(Product, id=item_id)
        try:
            cart = Cart(request)
            if action == "add":
                print("add")
                cart.add(product)

            elif action == "decrease":
                cart.decrease(product)
            context = {
                "item_count": cart.__len__(),
                "success": True,
                "quantity": cart.cart[item_id]["quantity"],
                "total": cart.cart[item_id]["quantity"] * cart.cart[item_id]["price"],
                "total_price": cart.get_total_price(),
                "total_discount": cart.get_total_discount(),
                "total_newprice": cart.get_total_after_price(),
            }

            return Response(context, status=status.HTTP_200_OK)
        except product.DoesNotExist:
            return Response(
                {"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND
            )


class RemoveItemView(APIView):
    def post(self, request):
        item_id = request.data.get("item_id")
        product = get_object_or_404(Product, id=item_id)
        try:
            cart = Cart(request)
            cart.remove(product)
            context = {
                "item_count": cart.__len__(),
                "success": True,
                "total_price": cart.get_total_price(),
                "total_discount": cart.get_total_discount(),
                "total_newprice": cart.get_total_after_price(),
            }
            return Response(context, status=status.HTTP_200_OK)

        except product.DoesNotExist:
            return Response(
                {"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND
            )


# class ActiveAddressView(LoginRequiredMixin, APIView):
#     def get(self, request):
#         # address_id = request.data.get("address_id")
#         address_id = request.query_params.get("address_id")
#         print(address_id)
#         user = request.user  # Get the logged-in user
#         address = get_object_or_404(
#             Address, id=address_id, user=user
#         )  # Ensure the address belongs to the user
#
#         address.activate()  # Assuming this method activates the address
#         address.save()  # Save the changes
#         return Response(
#             {"message": "Address activated successfully."}, status=status.HTTP_200_OK
#         )


class ActiveAddressView(LoginRequiredMixin, APIView):
    def get(self, request):
        address_id = request.query_params.get("address_id")
        if not address_id:
            return Response(
                {"message": "Address ID not provided."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        print(address_id)
        user = request.user  # Get the logged-in user
        address = get_object_or_404(
            Address, id=address_id, user=user
        )  # Ensure the address belongs to the user

        address.activate()  # Assuming this method activates the address
        return Response(
            {"message": "Address activated successfully."}, status=status.HTTP_200_OK
        )


class OrderCreateView(LoginRequiredMixin, APIView):
    def get(self, request):
        cart = Cart(request)
        if cart.__len__() == 0:
            return Response(
                {"message": "we have no cart."}, status=status.HTTP_404_NOT_FOUND
            )
        else:
            address = Address.objects.get(user=request.user, is_active=True)

            order = Order.objects.create(user=request.user, address=address)

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    quantity=item["quantity"],
                    price=item["price"],
                )
            cart.clear()
            order_id = order.id
            print(order_id)
            return Response(
                {"message": "Order created successfully.", "order_id": order_id},
                status=status.HTTP_200_OK,
            )


# class CouponApplyView(APIView):
#     serializer = CouponApplySerializer
#
#     def post(self, request, order_id):
#         now = datetime.datetime.now()
#         coupon_serializer = self.serializer(data=request.data)
#         if coupon_serializer.is_valid():
#             code = coupon_serializer.validated_data["code"]
#             try:
#                 coupon = Coupon.objects.get(code__exact=code, valid_from__lte=now, valid_to__gte=now)
#             except Coupon.DoesNotExist:
#                 return Response({"message": "Coupon does not exist"}, status=status.HTTP_404_NOT_FOUND)
#             order = Order.objects.get(id=order_id)
#             new_price = order.get_total_price()
#             order.discount = coupon.discount
#             order.save()
#             return Response({"message": "order discounted successfully apply", "new_price": new_price}, status=status.HTTP_200_OK)


class CouponApplyView(APIView):
    serializer_class = CouponApplySerializer

    def post(self, request, order_id):
        # now = datetime.datetime.now()
        coupon_serializer = self.serializer_class(data=request.data)

        if coupon_serializer.is_valid():
            code = coupon_serializer.validated_data["code"]
            print(code)
            try:
                coupon = Coupon.objects.get(code__exact=code, active=True)
            except Coupon.DoesNotExist:
                return Response(
                    {"message": "Coupon does not exist or is not valid"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            try:
                order = Order.objects.get(id=order_id)
            except Order.DoesNotExist:
                return Response(
                    {"message": "Order does not exist"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            # Apply the discount to the order
            order.discount = coupon.discount
            order.save()

            # Calculate the new price based on the discount
            new_price = order.get_total_price()

            return Response(
                {"message": "Order discounted successfully", "new_price": new_price},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                coupon_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
