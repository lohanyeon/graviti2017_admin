from django.conf.urls import patterns, url
from portfolios import views

urlpatterns = patterns('',
                       url(r'^$', views.Portfolio.as_view(), name='portfolio_list'),
                       url(r'^api/portfolio/$', views.json_portfolio_list),
                       url(r'^api/portfolio/(?P<pk>\d+)/$', views.json_portfolio_by_pk),
                       )
