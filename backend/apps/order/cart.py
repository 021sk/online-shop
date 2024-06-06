from apps.home.models import Product


class Cart(object):
    def __init__(self, request, *args, **kwargs):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 1,
                "price": product.price,
                "after_price": product.new_price,
                "discount": product.discount,
            }
        else:
            if self.cart[product_id]["quantity"] < product.inventory:
                self.cart[product_id]["quantity"] += 1
        self.save()

    def decrease(self, product):
        product_id = str(product.id)
        if self.cart[product_id]["quantity"] > 1:
            self.cart[product_id]["quantity"] -= 1
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def clear(self):
        del self.session["cart"]
        self.save()

    def get_total_price(self):
        total_price = sum(
            item["price"] * item["quantity"] for item in self.cart.values()
        )
        return total_price

    def get_total_discount(self):
        total_discount = sum(
            item["discount"] * item["quantity"] for item in self.cart.values()
        )
        return total_discount

    def get_total_after_price(self):
        total_price = sum(
            item["after_price"] * item["quantity"] for item in self.cart.values()
        )
        return total_price

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart_dict = self.cart.copy()
        for product in products:
            cart_dict[str(product.id)]["product"] = product
        for item in cart_dict.values():
            item["total"] = item["price"] * item["quantity"]
            yield item

    def save(self):
        self.session.modified = True
