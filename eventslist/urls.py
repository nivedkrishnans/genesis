from django.conf.urls import include, url
from . import views
import django.contrib.auth.views

urlpatterns = [
    url(r'^$', views.eventIndex, name='eventIndex'),
    url(r'^details$', views.details, name='details'),
    url(r'^details/$', views.details, name='details'),

]
