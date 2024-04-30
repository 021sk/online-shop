from django.contrib.auth import authenticate, login, get_user_model
from django.http import response
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from utils import catche, mail
from django.core.cache import cache

from uuid import uuid4

User = get_user_model()


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(generic.View):
    template_name = "public/login-password.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request):
        username = self.request.POST.get("username", None)
        password = self.request.POST.get("password", None)

        if not all((username, password)):
            return response.HttpResponse(
                "'username' or 'password' should not be null !", status=400
            )

        if user := authenticate(password=password, username=username):
            if user.is_active:
                login(self.request, user)
                return redirect("home")

            # create token and activate
            if not catche.get_or_create(
                f"activate_token_user_{user.username}", lambda: uuid4().hex, 300
            ):
                print(cache.get(f"activate_token_user_{user.username}"))
                # send_verification_code
                mail.send_mail(
                    f"Verification {user.username}",
                    user.email,
                    "mail/verfication.html",
                    {
                        "user": user,
                        "token": cache.get(f"activate_token_user_{user.username}"),
                        "host": self.request.get_host(),
                    },
                )
            return redirect("public_activate_page")

        return response.HttpResponse("User not found !", status=404)


class VerificationView(generic.View):
    template_name = "pages/verify_successfull.html"

    def get(self, request, username, token):
        user = get_object_or_404(User, username=username)
        if (
            not (token_in_cache := cache.get(f"activate_token_user_{user.username}"))
            or token_in_cache != token
        ):
            # print(token_in_cache)
            return response.HttpResponse("Your link has expired!", status=400)

        user.is_active = True
        user.save(update_fields=["is_active"])

        # login:
        login(self.request, user)
        cache.delete(f"activate_token_user_{user.username}")

        return render(request, self.template_name)
