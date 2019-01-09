from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import essentials.views
import originals.views
import registration.views
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    url(r'^cp/demigod/', admin.site.urls),
	url(r'^$', essentials.views.home , name="home"),
    url(r'^registration/', include('registration.urls')),
    url(r'^register/',registration.views.redirectRegistrationIndex),
	url(r'^updates/$', essentials.views.updates , name="updates"),
    url(r'^events/', include('essentials.urls')),
	url(r'^help/$', essentials.views.FaqListView.as_view() , name="help"),
	url(r'^contact/$', essentials.views.contact , name="contact"),
	url(r'^partners/$', essentials.views.partners , name="partners"),
    url(r'^sponsors/$', essentials.views.sponsors , name="sponsors"),
    url(r'^originals/$', originals.views.originals , name="originals"),
	url(r'^archive/$', originals.views.archive , name="archive"),
	url(r'^policy/$', essentials.views.policy , name="policy"),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name="robots"),
	url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/plain'), name="sitemap"),
	url(r'^2018/$', views.pravega2018 , name="pravega2018"),
	url(r'^2017/$', views.pravega2017 , name="pravega2017"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
