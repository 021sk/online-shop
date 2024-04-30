from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend as BaseBackend
import re

User = get_user_model()


class ModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        phone_validator = re.search(
            "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", username
        )
        if username is None or password is None:
            return

        try:
            user = User.objects.get(
                **({"phone": username} if phone_validator else {"username": username})
            )
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)

        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def user_can_authenticate(self, user):
        return True
