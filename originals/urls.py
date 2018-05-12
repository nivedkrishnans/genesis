from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.originals_all, name='originals_all'),
	url(r'^blogs/$', views.blogs, name='blogs'),
	url(r'^sciencequizzine$', views.sciencequizzine, name='sciencequizzine'),
	url(r'^comicstrips$', views.comicstrips, name='comicstrips'),
	url(r'^tuesdaytrivia$', views.tuesdaytrivia, name='tuesdaytrivia'),
	url(r'^throwbackthursdays$', views.throwbackthursdays, name='throwbackthursdays'),
	url(r'^memes$', views.memes, name='memes'),
	url(r'^videos$', views.videos, name='videos'),
]
