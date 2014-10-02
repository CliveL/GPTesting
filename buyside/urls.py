__author__ = 'Clive'
from django.conf.urls import patterns, url

from buyside import views

urlpatterns = patterns('',
                       # ex: /buyside/VAGABC123456789/
                       # ex: /buyside/homepage.html
                       url(r'^homepage/$', views.homepage, name='homepage'),
                       # ex: /buyside/vehicleconfirm/
                       url(r'^vehicleconfirm/$', views.vehicleconfirm, name="vehicleconfirm"),
                       # ex: /buyside/vehicleconfirm/
                       url(r'^treelist/$', views.treelist, name="treelist"),
                       # this is the entry point if someone has Googled a specific part
                       url(r'^(?P<search_id_1>\w+)/$', views.search, name='search'),
                       # add search if someone has a specific car, i.e. the have come from homepage
                       # url may be copy and pasted to be sent in an e-mail
                       url(r'^(?P<search_id_1>\w+)/(?P<search_id_2>\w+)/$', views.search, name='search2'),
)