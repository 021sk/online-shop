from apps.core.models import TimeStampMixin, LogicalMixin
from django.urls import reverse
from django.db import models


class Category(models.Model):
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    sub_category = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subcategory",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]

    def get_absolute_url(self):
        return reverse(
            "product:product-list-filter",
            args=[
                self.slug,
            ],
        )

    def __str__(self):
        return self.name


class Product(TimeStampMixin, LogicalMixin):
    category = models.ManyToManyField(Category, related_name="products")
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    available = models.BooleanField(default=True)
    inventory = models.PositiveIntegerField(default=0)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.PositiveIntegerField(
        default=0,
    )
    new_price = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["-create_at"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-create_at"]),
        ]

    def get_absolute_url(self):
        return reverse(
            "product:product-detail",
            args=[
                self.slug,
            ],
        )

    def __str__(self):
        return self.name


class Image(TimeStampMixin):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
    )
    file = models.ImageField(upload_to="product_images/%Y/%m/%d")
    title = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ["-create_at"]
        indexes = [models.Index(fields=["-create_at"])]

    def __str__(self):
        return self.title


class ProductFeature(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    product = models.ForeignKey(
        Product, related_name="features", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name + ":" + self.value
