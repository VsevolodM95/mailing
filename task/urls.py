from django.conf.urls import patterns, include, url
from qons import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^qons/', include('qons.urls', namespace="qons")),
    url(r'^qons/(?P<qon_id>\d+)/results/$', views.results, name='results'),
    url(r'^admin/', include(admin.site.urls)),
)
