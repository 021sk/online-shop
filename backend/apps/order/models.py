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

    def __str__(self):
        return f"{self.user} - {str(self.id)}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)


class coupon(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="coupons"
    )
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField()
    active = models.BooleanField(default=False)
