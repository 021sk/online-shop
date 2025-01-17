from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models import TimeStampMixin, LogicalMixin
from apps.accounts.manager import UserManager
from django.core.validators import RegexValidator


class User(AbstractUser, TimeStampMixin, LogicalMixin):
    phone = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                r"^(0|\+98)?9[0-4][0-9]{8}$",
                "invalid phone number",
            )
        ],
    )
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

    # def save(self, *args, **kwargs):
    #     if not self.is_superuser:
    #         self.set_password(self.password)
    #     super().save(*args, **kwargs)
    #


class Address(TimeStampMixin, LogicalMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    address = models.TextField()
    city = models.CharField(max_length=20, blank=True)
    province = models.CharField(max_length=20, blank=True)

    def activate(self):
        # Deactivate all other addresses for the same user
        self.user.addresses.exclude(id=self.id).update(is_active=False)
        # Activate this address
        self.is_active = True
        self.save(update_fields=["is_active"])
