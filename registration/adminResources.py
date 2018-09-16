from .models import *
from django.utils.html import format_html
from django.conf import settings

def superuser_fields(self, request, obj=None, only_superuser_fieldslist=[]):   #for maiking all fields read only for non superuser staff accounts
    if request.user.is_staff:
        if request.user.is_superuser:
            return only_superuser_fieldslist
        else:
            return [f.name for f in self.model._meta.fields]


def seeVideoFile(self, obj):    #for showings uploaded video link in the list of model instances
    try:
        if obj.videoFile:
            temp = '<a href="%s/%s">%s</a>' % (settings.MEDIA_URL,obj.videoFile, "Video")
        else:
            temp = '-'
    except:
        temp = '-'
    return format_html(temp)


def seeVideoLink(self, obj):     #for showings external video link in the list of model instances
    try:
        if obj.videoFileLink:
            temp = '<a href="%s">%s</a>' % (obj.videoFileLink, "Link")
        else:
            temp = '-'
    except:
        temp = '-'
    return format_html(temp)
