from django.conf.urls import patterns, include, url
from mysite.views import home
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^$',home),
    url(r'^polls/',include('polls.urls',namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
)
