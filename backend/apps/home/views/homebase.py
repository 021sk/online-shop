# Create your views here.
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "public/index.html"
