from django.contrib import admin
from .models import *
from . import adminResources
from import_export.admin import ExportMixin
from django.utils.html import format_html
from django.conf import settings



class UserDataResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','institution','city',)
    list_filter = ('email_validated','institution','city',)
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    class Meta:
        model = UserData

class AdminEventResource(ExportMixin,admin.ModelAdmin):
    fields = ('title','registrationStatus','description','registrationLink')    #for showing the fields in this order
    list_display = ('title','registrationStatus')
    list_filter = ('registrationStatus',)
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_staff:
            if request.user.is_superuser:
                return []
            else:
                return ['title','registrationLink']
    class Meta:
        model = AdminEvent


class CampusAmbassadorResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','institution','city','submit_date',)
    list_filter = ('submit_date','institution','city',)
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj,)
    class Meta:
        model = CampusAmbassador



class LasyaRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','teamName','teamLeader','email','institution','city','submit_date','seeVideoFile','seeVideoLink',)
    list_filter = ('submit_date','institution','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj,)
    def seeVideoFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeVideoFile(self, obj)
    def seeVideoLink(self, obj):                         #shows external video link in the list of model instances
        return adminResources.seeVideoLink(self, obj)

    class Meta:
        model = LasyaRegistration

class ProsceniumRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','teamName','teamLeader','email','institution','city','submit_date','seeVideoFile','seeVideoLink')
    list_filter = ('submit_date','institution','city',)
    readonly_fields = ('videoFile','videoFileLink',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    def seeVideoFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeVideoFile(self, obj)
    def seeVideoLink(self, obj):                         #shows external video link in the list of model instances
        return adminResources.seeVideoLink(self, obj)

    class Meta:
        model = ProsceniumRegistration


class BattleOfBandsRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','teamName','teamLeader','email','institution','city','submit_date','seeAudioVideoFile','seeAudioVideoLink')
    list_filter = ('submit_date','institution','city',)
    readonly_fields = ('audioVideoFile','audioVideoFileLink',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    def seeAudioVideoFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeAudioVideoFile(self, obj)
    def seeAudioVideoLink(self, obj):                         #shows external video link in the list of model instances
        return adminResources.seeAudioVideoLink(self, obj)

    class Meta:
        model = BattleOfBandsRegistration


class FootprintsRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','teamName','teamLeader','email','institution','city','submit_date')
    list_filter = ('submit_date','institution','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = FootprintsRegistration


class DecoherenceRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('teamName','institution','city','submit_date')
    list_filter = ('submit_date','institution','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = DecoherenceRegistration

admin.site.register(UserData,UserDataResource)
admin.site.register(AdminEvent,AdminEventResource)
admin.site.register(CampusAmbassador,CampusAmbassadorResource)
admin.site.register(LasyaRegistration,LasyaRegistrationResource)
admin.site.register(ProsceniumRegistration,ProsceniumRegistrationResource)
admin.site.register(BattleOfBandsRegistration,BattleOfBandsRegistrationResource)
admin.site.register(FootprintsRegistration,FootprintsRegistrationResource)
admin.site.register(DecoherenceRegistration,DecoherenceRegistrationResource)
