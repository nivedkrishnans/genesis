from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import essentials.views
import originals.views
import registration.views
from . import views

urlpatterns = [
    url(r'^demigod/', admin.site.urls),
	url(r'^$', essentials.views.home , name="home"),
    url(r'^registration/', include('registration.urls')),
	url(r'^updates/$', essentials.views.updates , name="updates"),
    url(r'^events/', include('essentials.urls')),
	url(r'^help/$', essentials.views.comingsoon , name="help"),
	url(r'^contact/$', essentials.views.contact , name="contact"),
	url(r'^partners/$', essentials.views.partners , name="partners"),
	url(r'^register/$', essentials.views.register , name="register"),
    url(r'^originals/$', originals.views.originals , name="originals"),
	url(r'^archive/$', originals.views.archive , name="archive"),
	url(r'^policy/$', essentials.views.policy , name="policy"),
	url(r'^2018/$', views.pravega2018 , name="pravega2018"),
	url(r'^2017/$', views.pravega2017 , name="pravega2017"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
