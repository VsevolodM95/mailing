from django.conf.urls import patterns, url

from qons import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^(?P<qon_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<qon_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<qon_id>\d+)/results/$', views.results, name='results'),
)
