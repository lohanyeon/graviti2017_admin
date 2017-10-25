from django.views.generic import TemplateView
from django.views.generic import TemplateView, ListView, DetailView
from portfolios.models import portfolio


class IndexView(TemplateView):
    template_name = 'index.html'