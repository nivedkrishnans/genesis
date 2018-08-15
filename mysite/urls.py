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
    url(r'^events/$', essentials.views.events , name="events"),
	url(r'^help/$', essentials.views.comingsoon , name="help"),
	url(r'^contact/$', essentials.views.contact , name="contact"),
	url(r'^partners/$', essentials.views.partners , name="partners"),
	url(r'^register/$', essentials.views.register , name="register"),
    url(r'^originals/$', originals.views.originals , name="originals"),
	url(r'^archive/$', originals.views.archive , name="archive"),
	url(r'^proscenium/$', essentials.views.proscenium , name="proscenium"),
	url(r'^lasya/$', essentials.views.lasya , name="lasya"),
	url(r'^footprints/$', essentials.views.footprints , name="footprints"),
	url(r'^battleofbands/$', essentials.views.battleofbands , name="battleofbands"),
	url(r'^2018/$', views.pravega2018 , name="pravega2018"),
	url(r'^2017/$', views.pravega2017 , name="pravega2017"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
