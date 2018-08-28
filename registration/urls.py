from django.conf.urls import include, url
from . import views
import django.contrib.auth.views

#havev;t been abale to get custom password reset templates


urlpatterns = [
	url(r'^signup$', views.signup, name='signup'),
	url(r'^activate/account/$', views.activateAccount),
	url(r'^$', views.redirectLogin),
	url(r'^', include('django.contrib.auth.urls')),
]
