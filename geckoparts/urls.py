from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geckoparts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^buyside/', include('buyside.urls', namespace='buyside')),
    url(r'^admin/', include(admin.site.urls)),
)
