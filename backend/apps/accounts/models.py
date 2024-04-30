from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models import TimeStampMixin, LogicalMixin
from apps.accounts.manager import UserManager


class User(AbstractUser, TimeStampMixin, LogicalMixin):
    phone = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField("active", default=False)
    email = models.EmailField()

    class Meta:
        indexes = [
            models.Index(fields=["username"]),
            models.Index(fields=["email"]),
        ]

    def __str__(self):
        return self.first_name + " " + self.last_name

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def save(self, *args, **kwargs):
        if not self.is_superuser:
            self.set_password(self.password)
        super().save(*args, **kwargs)


class Address(TimeStampMixin, LogicalMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    address = models.TextField()

    # def activate(self):
    #     # Deactivate all other addresses for the same user
    #     self.user.addresses.exclude(id=self.id).update(is_active=False)
    #     # Activate this address
    #     self.is_active = True
    #     self.save(update_fields=["is_active"])
