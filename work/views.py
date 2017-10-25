from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from portfolios.models import portfolio


# Create your views here.
class WorkView(TemplateView):
    template_name = "work.html"
