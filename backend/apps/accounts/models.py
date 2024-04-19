from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.core.models import TimeStampMixin, LogicalMixin


class User(AbstractUser, TimeStampMixin, LogicalMixin):
    phone = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Address(TimeStampMixin, LogicalMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    address = models.TextField()

    # def activate(self):
    #     # Deactivate all other addresses for the same user
    #     self.user.addresses.exclude(id=self.id).update(is_active=False)
    #     # Activate this address
    #     self.is_active = True
    #     self.save(update_fields=["is_active"])
