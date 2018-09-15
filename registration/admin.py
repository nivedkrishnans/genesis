from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from django.conf import settings



class UserDataResource(ImportExportModelAdmin):
    list_display = ('user','institution','city',)
    list_filter = ('email_validated','institution','city',)
    class Meta:
        model = UserData

class AdminEventResource(ImportExportModelAdmin):
    list_display = ('title','registrationStatus')
    list_filter = ('registrationStatus',)
    class Meta:
        model = AdminEvent

class LasyaRegistrationResource(ImportExportModelAdmin):
    list_display = ('user','teamName','teamLeader','institution','city','submit_date','seeVideoFile','seeVideoLink',)
    list_filter = ('submit_date','institution','city',)
    readonly_fields = ('videoFile','videoFileLink',)
    def seeVideoFile(self, obj):
        try:
            if obj.videoFile:
                temp = '<a href="%s/%s">%s</a>' % (settings.MEDIA_URL,obj.videoFile, "Video")
            else:
                temp = '-'
        except:
            temp = '-'
        return format_html(temp)
    def seeVideoLink(self, obj):
        try:
            if obj.videoFileLink:
                temp = '<a href="%s">%s</a>' % (obj.videoFileLink, "Link")
            else:
                temp = '-'
        except:
            temp = '-'
        return format_html(temp)
    class Meta:
        model = LasyaRegistration

class ProsceniumRegistrationResource(ImportExportModelAdmin):
    list_display = ('user','teamName','teamLeader','institution','city','submit_date','seeVideoFile','seeVideoLink')
    list_filter = ('submit_date','institution','city',)
    readonly_fields = ('videoFile','videoFileLink',)
    def seeVideoFile(self, obj):
        try:
            if obj.videoFile:
                temp = '<a href="%s/%s">%s</a>' % (settings.MEDIA_URL,obj.videoFile, "Video")
            else:
                temp = '-'
        except:
            temp = '-'
        return format_html(temp)
    def seeVideoLink(self, obj):
        try:
            if obj.videoFileLink:
                temp = '<a href="%s">%s</a>' % (obj.videoFileLink, "Link")
            else:
                temp = '-'
        except:
            temp = '-'
        return format_html(temp)
    class Meta:
        model = ProsceniumRegistration

class FootprintsRegistrationResource(ImportExportModelAdmin):
    list_display = ('user','teamName','teamLeader','institution','city','submit_date')
    list_filter = ('submit_date','institution','city',)
    class Meta:
        model = FootprintsRegistration



admin.site.register(UserData,UserDataResource)
admin.site.register(AdminEvent,AdminEventResource)
admin.site.register(LasyaRegistration,LasyaRegistrationResource)
admin.site.register(ProsceniumRegistration,ProsceniumRegistrationResource)
admin.site.register(FootprintsRegistration,FootprintsRegistrationResource)
