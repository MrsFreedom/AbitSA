from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='main'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^bacalavr/$', views.bacalavr, name='bacalavr'),
    url(r'^magistr/$', views.magistr, name='magistr'),
    url(r'^aspir/$', views.aspir, name='aspir'),
    url(r'^prog_bac/$', views.prog_bac, name='prog_bac'),
    url(r'^teacher/$', views.teacher, name='teacher'),
    url(r'^home/$', views.home, name='home'),
    url(r'^map/$', views.map, name='map'),
    url(r'^mentor_detal/(?P<pk>\d+)$', views.mentor_detal, name='mentor_detal'),


]
