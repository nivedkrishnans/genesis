from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import essentials.views
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', essentials.views.home , name="home"),
	url(r'^originals/', include('originals.urls')),
	url(r'^2018/$', views.pravega2018 , name="pravega2018"),
	url(r'^2017/$', views.pravega2017 , name="pravega2017"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
