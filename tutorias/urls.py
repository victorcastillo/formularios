from django.conf.urls.defaults import patterns,  url

urlpatterns = patterns('',
    url(r'^proceso_administrativo/$', 'tutorias.views.proceso_administrativo', name='proceso_administrativo'),
    url(r'^proceso_administrativo_proceso/$', 'tutorias.views.proceso_administrativo_proceso', name='proceso_administrativo_proceso'),
    url(r'^motivo/$', 'tutorias.views.motivo', name='motivo'),
    url(r'^servicio/$', 'tutorias.views.servicio', name='servicio'),
)
