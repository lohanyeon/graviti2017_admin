"""graviti_2017 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from graviti2017 import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^portfolios/', include('portfolios.urls', namespace="portfolios")),
    url(r'^about/', include('about.urls', namespace="about")),
    url(r'^work/', include('work.urls', namespace="work")),
    url(r'^contact/', include('contact.urls', namespace="contact")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
