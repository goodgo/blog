from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'hello'),
    url(r'^systime/$', 'systime'),
    url(r'^current_time/$', 'current_time'),
    url(r'^meta/$', 'meta'),
    url(r'^search/$', 'search'),
    url(r'^contact/$', 'contact'),
)
