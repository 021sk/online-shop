from rest_framework.views import APIView
from rest_framework.response import Response
from ..cart import Cart
from django.shortcuts import get_object_or_404
from apps.home.models import Product
from rest_framework import status


class CartAddApiView(APIView):
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
