from django.conf.urls import url
from . import views
import  originals.views

urlpatterns = [
	url(r'^$', views.events , name="events"),
	url(r'^proscenium/$', views.proscenium , name="proscenium"),
	url(r'^lasya/$', views.lasya , name="lasya"),
	url(r'^footprints/$', views.footprints , name="footprints"),
	url(r'^battleofbands/$', views.battleofbands , name="battleofbands"),
	url(r'^decoherence/$', views.decoherence , name="decoherence"),
	url(r'^wikimediaphotography/$', views.wikimediaphotography , name="wikimediaphotography"),
	url(r'^inotherwords/$', originals.views.InOtherWords , name="inotherwords"),
	url(r'^inotherwords/ch01$', originals.views.IOW_challenge01 , name="iow_challenge01"),
	url(r'^inotherwords/ch02$', originals.views.IOW_challenge02 , name="iow_challenge02"),
	url(r'^inotherwords/ch03$', originals.views.IOW_challenge03 , name="iow_challenge03"),
	url(r'^inotherwords/ch04$', originals.views.IOW_challenge04 , name="iow_challenge04"),
	url(r'^inotherwords/ch05$', originals.views.IOW_challenge05 , name="iow_challenge05"),
]
