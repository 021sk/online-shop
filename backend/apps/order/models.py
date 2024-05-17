from django.db import models
from django.contrib.auth import get_user_model
from apps.core.models import TimeStampMixin, LogicalMixin
from apps.home.models import Product


class Order(TimeStampMixin, LogicalMixin):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="orders"
    )
    paid = models.BooleanField(default=False)
    discount = models.IntegerField(blank=True, null=True, default=None)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        return total

    def __str__(self):
        return f"{self.user} - {str(self.id)}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return str(self.id)


class coupon(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="coupons"
    )
    code = models.CharField(max_length=30, unique=True, default=None)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code
