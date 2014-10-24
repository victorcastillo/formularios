from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tutorias/', include('tutorias.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ventas/', include('ventas.urls')),
)
