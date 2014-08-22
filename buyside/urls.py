__author__ = 'Clive'
from django.conf.urls import patterns, url

from buyside import views

urlpatterns = patterns('',
                       # ex: /buyside/search/
                       url(r'^search/$', views.search, name='search'),
                       # ex: /buyside/homepage.html
                       url(r'^homepage/$', views.homepage, name='homepage'),
                       # ex: /buyside/vehicleconfirm/
                       url(r'^vehicleconfirm/$', views.vehicleconfirm, name="vehicleconfirm"),
                       # ex: /buyside/vehicleconfirm/
                       url(r'^treelist/$', views.treelist, name="vehicleconfirm"),
)