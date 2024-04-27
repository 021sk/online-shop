from django.contrib.auth import authenticate, login
from django.http import response
from django.shortcuts import render, redirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


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

        return response.HttpResponse("User not found !", status=404)
