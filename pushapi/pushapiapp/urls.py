from django.conf.urls import patterns, url
from pushapiapp import views

urlpatterns = patterns('',
    url(r'^door-status/$', views.door_status, name='door_status'),
)
