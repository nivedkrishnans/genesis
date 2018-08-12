from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^memes$', views.memes, name='memes'),
]
