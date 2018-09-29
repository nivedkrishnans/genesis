from django.conf.urls import url
from . import views
import  originals.views

urlpatterns = [
	url(r'^$', views.events , name="events"),
	url(r'^proscenium/$', views.proscenium , name="proscenium"),
	url(r'^lasya/$', views.lasya , name="lasya"),
	url(r'^footprints/$', views.footprints , name="footprints"),
	url(r'^battleofbands/$', views.battleofbands , name="battleofbands"),
	url(r'^inotherwords/$', originals.views.InOtherWords , name="inotherwords"),
	url(r'^inotherwords/ch01$', originals.views.IOW_challenge01 , name="iow_challenge01"),
	url(r'^inotherwords/ch02$', originals.views.IOW_challenge02 , name="iow_challenge02"),
]
