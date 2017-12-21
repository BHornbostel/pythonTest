from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^register$', views.register), 
    url(r'^login$', views.login), 
    url(r'^logout$', views.logout), 
    url(r'^travels$', views.home),
    url(r'^travels/add$', views.create),
    url(r'^travels/add_trip$', views.add),
    url(r'^user/(?P<number>\d)$', views.user),
    url(r'^travels/destination/(?P<number>\d)$', views.destination),
     url(r'^travels/join/(?P<number>\d)$', views.join),
     url(r'^logout$',views.logout)
    
]