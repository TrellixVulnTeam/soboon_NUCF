from django.conf.urls import url
from . import views

urlpatterns = [
 #   url(r'^$', views.index, name='index'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^blog/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
#    url(r'^gallery/$', views.gallery, name='gallery'),
#    url(r'^about/$', views.about, name='about'),
    ]