from django.conf.urls.defaults import patterns,  url

urlpatterns = patterns('',
    url(r'^venta/$', 'ventas.views.venta', name='venta'),
)
