from django.conf.urls import url, include
#from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.validate),
    url(r'^login$', views.success)
]
