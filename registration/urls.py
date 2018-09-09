from django.conf.urls import include, url
from . import views
import django.contrib.auth.views

#havev;t been abale to get custom password reset templates


urlpatterns = [
	url(r'^closed$', views.closed, name='closed'),
	url(r'^closed/$', views.closed, name='closed'),
	url(r'^registered$', views.registered, name='registered'),
	url(r'^registered/$', views.registered, name='registered'),
	url(r'^lasya$', views.lasyaRegistration, name='lasyaRegistration'),
	url(r'^lasya/$', views.lasyaRegistration, name='lasyaRegistration'),
	url(r'^proscenium$', views.prosceniumRegistration, name='prosceniumRegistration'),
	url(r'^proscenium/$', views.prosceniumRegistration, name='prosceniumRegistration'),
	url(r'^footprints$', views.footprintsRegistration, name='footprintsRegistration'),
	url(r'^footprints/$', views.footprintsRegistration, name='footprintsRegistration'),
	url(r'^signup$', views.signup, name='signup'),	url(r'^signup$', views.signup, name='signup'),
	url(r'^signup/$', views.signup, name='signup'),	url(r'^signup$', views.signup, name='signup'),
	url(r'^activate/account/$', views.activateAccount),
	url(r'^$', views.registration_index, name="registration"),
	url(r'^', include('django.contrib.auth.urls')),
]
