from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.core.models import TimeStampMixin, LogicalMixin


class User(AbstractUser, TimeStampMixin, LogicalMixin):
    phone = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    address = models.TextField()
