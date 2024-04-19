from django.db import models
from apps.core.models import TimeStampMixin, LogicalMixin


class Category(models.Model):
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
        pass

    def __str__(self):
        return self.name


class Product(TimeStampMixin, LogicalMixin):
    category = models.ManyToManyField(Category, related_name="products")
    name = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200, unique=True)
    # image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    discount = models.PositiveIntegerField(
        default=0,
    )
    new_price = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        pass

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
    )
    file = models.ImageField(upload_to="")
    title = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title
