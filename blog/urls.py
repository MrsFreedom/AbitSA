from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
url(r'^base/$', views.base, name='base'),
    url(r'^sa/$', views.sa, name='sa'),
    url(r'^aphp/$', views.aphp, name='aphp'),
    url(r'^sapr/$', views.sapr, name='sapr'),
    url(r'^km/$', views.km, name='km'),
    url(r'^dostijenia/$', views.dostijenia, name='dostijenia'),
    url(r'^bacalavr/$', views.bacalavr, name='bacalavr'),
    url(r'^magistr/$', views.magistr, name='magistr'),
    url(r'^table/$', views.table, name='table'),


]
