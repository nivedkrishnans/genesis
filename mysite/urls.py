from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import essentials.views
import originals.views
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', essentials.views.home , name="home"),
	url(r'^updates/$', essentials.views.comingsoon , name="updates"),
    url(r'^events/$', essentials.views.comingsoon , name="events"),
	url(r'^help/$', essentials.views.comingsoon , name="help"),
	url(r'^contact/$', essentials.views.comingsoon , name="contact"),
	url(r'^archive/$', essentials.views.comingsoon , name="archive"),
	url(r'^partners/$', essentials.views.comingsoon , name="partners"),
	url(r'^register/$', essentials.views.comingsoon , name="register"),
    url(r'^archives/', essentials.views.comingsoon),
    url(r'^sciencequizzine/', originals.views.sciencequizzine),
    url(r'^originals/', include('originals.urls')),
	url(r'^2018/$', views.pravega2018 , name="pravega2018"),
	url(r'^2017/$', views.pravega2017 , name="pravega2017"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
