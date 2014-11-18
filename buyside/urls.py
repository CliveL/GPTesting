__author__ = 'Clive'
from django.conf.urls import patterns, url

from buyside import views

urlpatterns = patterns('',
                       # ex: /buyside/homepage.html
                       url(r'^homepage/$', views.homepage, name='homepage'),
                       # ex: /buyside/vehicle_confirm/
                       url(r'^vehicle_confirm/$', views.vehicle_confirm, name="vehicle_confirm"),
                       # ex: /buyside/vehicle_confirm/
                       url(r'^treelist/$', views.treelist, name="treelist"),
                       # ex: /buyside/vehicle_upload/
                       url(r'^vehicle_upload/(?P<vehicle_id>\w+)/$', views.vehicle_upload, name="vehicle_upload"),
                       # ex: /buyside/upload_complete/
                       url(r'^upload_complete/$', views.upload_complete, name="upload_complete"),
                       # ex: /buyside/VAGABC123456789/
                       # this is the entry point if someone has Googled a specific part
                       url(r'^shop/(?P<search_id_1>\w+)/$', views.search, name='search'),
                       # add search if someone has a specific car, i.e. the have come from homepage
                       # url may be copy and pasted to be sent in an e-mail
                       url(r'^shop/(?P<search_id_1>\w+)/(?P<search_id_2>\w+)/$', views.search, name='search2'),
)