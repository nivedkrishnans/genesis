from django.conf.urls import include, url
from . import views
import django.contrib.auth.views

#havev;t been abale to get custom password reset templates


urlpatterns = [
	url(r'^closed$', views.closed, name='closed'),
	url(r'^closed/$', views.closed, name='closed'),
	url(r'^registered$', views.registered, name='registered'),
	url(r'^registered/$', views.registered, name='registered'),
	url(r'^campusambassadors$', views.campusambassadors, name='campusambassadors'),
	url(r'^campusambassadors/$', views.campusambassadors, name='campusambassadors'),
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
	url('^password_reset/$', django.contrib.auth.views.PasswordResetView.as_view(
		'email_template_name'='registration/email_templates/password_reset.txt',
		'html_email_template_name'='registration/email_templates/reset_password_email.html',
		'subject_template_name'='registration/email_templates/password_reset_subject.txt'
	),name='password_reset'),
	url(r'^', include('django.contrib.auth.urls')),
]
