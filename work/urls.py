from django.conf.urls import patterns, url
from work import views

urlpatterns = patterns('',
                       url(r'^$', views.WorkView.as_view(), name='work'),
                       )