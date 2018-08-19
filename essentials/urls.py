from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.events , name="events"),
	url(r'^proscenium/$', views.proscenium , name="proscenium"),
	url(r'^lasya/$', views.lasya , name="lasya"),
	url(r'^footprints/$', views.footprints , name="footprints"),
	url(r'^battleofbands/$', views.battleofbands , name="battleofbands"),
]
