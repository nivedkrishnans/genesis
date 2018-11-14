from django.conf.urls import include, url
from . import views
import django.contrib.auth.views

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
	url(r'^decoherence$', views.decoherenceRegistration, name='decoherenceRegistration'),
	url(r'^decoherence/$', views.decoherenceRegistration, name='decoherenceRegistration'),
	url(r'^battleofbands$', views.battleofbandsRegistration, name='battleofbandsRegistration'),
	url(r'^battleofbands/$', views.battleofbandsRegistration, name='battleofbandsRegistration'),
	url(r'^ppp$', views.pppRegistration, name='pppRegistration'),
	url(r'^ppp/$', views.pppRegistration, name='pppRegistration'),
	url(r'^vignettora$', views.vignettoraRegistration, name='vignettoraRegistration'),
	url(r'^vignettora/$', views.vignettoraRegistration, name='vignettoraRegistration'),
	url(r'^impromptoo$', views.impromptooRegistration, name='impromptooRegistration'),
	url(r'^impromptoo/$', views.impromptooRegistration, name='impromptooRegistration'),
	url(r'^wikimediaphotography$', views.pppRegistration, name='wikimediaphotographyRegistration'),
	url(r'^wikimediaphotography/$', views.pppRegistration, name='wikimediaphotographyRegistration'),
	url(r'^pravega_innovation_summit$', views.pisRegistration, name='pisRegistration'),
	url(r'^pravega_innovation_summit/$', views.pisRegistration, name='pisRegistration'),
	url(r'^signup$', views.signup, name='signup'),	url(r'^signup$', views.signup, name='signup'),
	url(r'^signup/$', views.signup, name='signup'),	url(r'^signup$', views.signup, name='signup'),
	url(r'^activate/account/$', views.activateAccount),
	url(r'^$', views.registration_index, name="registration"),
	url('^password_reset/$', django.contrib.auth.views.PasswordResetView.as_view(
		email_template_name='registration/email_templates/password_reset.txt',
		html_email_template_name='registration/email_templates/reset_password_email.html',
		subject_template_name='registration/email_templates/password_reset_subject.txt'
	),name='password_reset'),
	url(r'^', include('django.contrib.auth.urls')),
]
