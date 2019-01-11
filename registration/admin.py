from django.contrib import admin
from .models import *
from . import adminResources
from import_export.admin import ExportMixin
from django.utils.html import format_html
from django.conf import settings



class UserDataResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','institution','city','create_date')
    list_filter = ('email_validated','city','create_date')
    search_fields = ('full_name','institution','city','create_date','email','contact')
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    class Meta:
        model = UserData

class AdminEventResource(ExportMixin,admin.ModelAdmin):
    fields = ('title','displayTitle','registrationStatus','description','priority','registrationLink')    #for showing the fields in this order
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
    list_filter = ('submit_date','city',)
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj,)
    class Meta:
        model = CampusAmbassador

class VignettoraRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'full_name' ,'email','institution','city','submit_date')
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    class Meta:
        model = VignettoraRegistration

class ScienceJournalismRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'full_name' ,'email','institution','city','submit_date','seeArticleFile')
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    def seeArticleFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeArticleFile(self, obj)
    class Meta:
        model = ScienceJournalismRegistration

class ScienceJournalismSubmissionResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'title','submit_date','seeArticleFile')
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    def seeArticleFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeArticleFile(self, obj)
    class Meta:
        model = ScienceJournalismSubmission



class ETCRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','full_name','year','major', 'email','institution','city','submit_date')
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    class Meta:
        model = ETCRegistration


class LasyaRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','category','teamName','teamLeader','email','institution','city','submit_date','seeVideoFile','seeVideoLink',)
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj,)
    def seeVideoFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeVideoFile(self, obj)
    def seeVideoLink(self, obj):                         #shows external video link in the list of model instances
        return adminResources.seeVideoLink(self, obj)

    class Meta:
        model = LasyaRegistration


class LasyaSoloRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','full_name','institution','city','submit_date','seeVideoFile','seeVideoLink',)
    list_filter = ('submit_date',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj,)
    def seeVideoFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeVideoFile(self, obj)
    def seeVideoLink(self, obj):                         #shows external video link in the list of model instances
        return adminResources.seeVideoLink(self, obj)

    class Meta:
        model = LasyaSoloRegistration


class LasyaGroupRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','teamName','teamLeader','institution','city','submit_date','seeVideoFile','seeVideoLink',)
    list_filter = ('submit_date',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj,)
    def seeVideoFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeVideoFile(self, obj)
    def seeVideoLink(self, obj):                         #shows external video link in the list of model instances
        return adminResources.seeVideoLink(self, obj)

    class Meta:
        model = LasyaGroupRegistration

class ProsceniumRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','teamName','teamLeader','email','institution','city','submit_date','seeVideoFile','seeVideoLink')
    list_filter = ('submit_date','city',)
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
    list_display = ('user','teamName','teamLeader','email','institution','city','regionalfinalscity','submit_date','seeAudioVideoFile','seeAudioVideoLink')
    list_filter = ('submit_date','regionalfinalscity',)
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
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = FootprintsRegistration


class DecoherenceRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('teamName','institution','city','submit_date')
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = DecoherenceRegistration

class ChemisticonRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('teamName','institution','city','submit_date')
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = ChemisticonRegistration

class MolecularMuralsRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('teamName','institution','city','submit_date')
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = MolecularMuralsRegistration

class DebubularyRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('teamName','institution','city','submit_date')
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = DebubularyRegistration

class CryptothlonRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('teamName','institution','city','submit_date')
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = CryptothlonRegistration

class WikimediaPhotographyRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','wikimediaUsername','institution','city','submit_date')
    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    class Meta:
        model = WikimediaPhotographyRegistration


class ISCRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'full_name' ,'email','institution','city','submit_date')
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = ISCRegistration

class BaseISCRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'school_name','school_contact','email','city','submit_date')
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = BaseISCRegistration

class IBMHackathonRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'teamName' ,'email','institution','city','submit_date')
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    def seeArticleFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeArticleFile(self, obj)
    class Meta:
        model = IBMHackathonRegistration

class ETCRegisteredRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'submit_date','seeVideoFile','seeVideoLink',)
    list_filter = ('submit_date',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    def seeVideoFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeVideoFile(self, obj)
    def seeVideoLink(self, obj):                         #shows external video link in the list of model instances
        return adminResources.seeVideoLink(self, obj)

    class Meta:
        model = ETCRegisteredRegistration

class VignettoraRegisteredRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'submit_date','seeArticleFile','seeArticleLink',)
    list_filter = ('submit_date',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)
    def seeArticleFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeArticleFile(self, obj)
    def seeArticleLink(self, obj):                         #shows external video link in the list of model instances
        return adminResources.seeArticleLink(self, obj)

    class Meta:
        model = VignettoraRegisteredRegistration

class PISRound2RegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'submit_date','societalImpact','viability','originality','implementaton','totalScore','seeVideoFile','seeVideoLink')
    list_filter = ('submit_date',)

    def totalScore(self, obj):                        #shows calculated total score
        return (obj.societalImpact + obj.viability + obj.originality + obj.implementaton)
    def seeVideoFile(self, obj):                        #shows uploaded video link in the list of model instances`
        return adminResources.seeVideoFile(self, obj)
    def seeVideoLink(self, obj):                         #shows external video link in the list of model instances
        return adminResources.seeVideoLink(self, obj)

    class Meta:
        model = PISRound2Registration

class PUBGRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user', 'full_name' ,'city','submit_date')
    list_filter = ('submit_date','city',)

    def get_readonly_fields(self, request, obj=None):   #makes all fields read only for non superuser staff accounts
        return adminResources.superuser_fields(self, request, obj)

    class Meta:
        model = PUBGRegistration

class PISRegistrationResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','teamName','institution','city','submit_date')

    class Meta:
        model = PISRegistration

class StatusDatesResource(ExportMixin,admin.ModelAdmin):
    list_display = ('title','dtValue','description')
    class Meta:
        model = StatusDates

class DecoherencePrelimResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','decoherenceRegistration','submit_date','teamName','institution','city')
    class Meta:
        model = DecoherencePrelim

class DecoherenceObjectiveQuestionResource(ExportMixin,admin.ModelAdmin):
    list_display = ('qNo','title','text')
    class Meta:
        model = DecoherenceObjectiveQuestion

class DecoherenceSubjectiveQuestionResource(ExportMixin,admin.ModelAdmin):
    list_display = ('qNo','title','text')
    class Meta:
        model = DecoherenceSubjectiveQuestion


class CryptothlonPrelimResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','teamName','cryptothlonRegistration','submit_date','institution','city')
    class Meta:
        model = CryptothlonPrelim

class CryptothlonPrelimDumpResource(ExportMixin,admin.ModelAdmin):
    list_display = ('user','create_date','dumpString')
    class Meta:
        model = CryptothlonPrelimDump

admin.site.register(UserData,UserDataResource)
admin.site.register(AdminEvent,AdminEventResource)
admin.site.register(CampusAmbassador,CampusAmbassadorResource)
admin.site.register(LasyaRegistration,LasyaRegistrationResource)
admin.site.register(LasyaSoloRegistration,LasyaSoloRegistrationResource)
admin.site.register(LasyaGroupRegistration,LasyaGroupRegistrationResource)
admin.site.register(ProsceniumRegistration,ProsceniumRegistrationResource)
admin.site.register(BattleOfBandsRegistration,BattleOfBandsRegistrationResource)
admin.site.register(FootprintsRegistration,FootprintsRegistrationResource)
admin.site.register(DecoherenceRegistration,DecoherenceRegistrationResource)
admin.site.register(ChemisticonRegistration,ChemisticonRegistrationResource)
admin.site.register(MolecularMuralsRegistration,MolecularMuralsRegistrationResource)
admin.site.register(WikimediaPhotographyRegistration,WikimediaPhotographyRegistrationResource)
admin.site.register(PISRegistration,PISRegistrationResource)
admin.site.register(ScienceJournalismRegistration,ScienceJournalismRegistrationResource)
admin.site.register(ScienceJournalismSubmission,ScienceJournalismSubmissionResource)
admin.site.register(DebubularyRegistration,DebubularyRegistrationResource)
admin.site.register(CryptothlonRegistration,CryptothlonRegistrationResource)
admin.site.register(CryptothlonPrelim,CryptothlonPrelimResource)
admin.site.register(CryptothlonPrelimDump,CryptothlonPrelimDumpResource)
admin.site.register(StatusDates,StatusDatesResource)
admin.site.register(DecoherencePrelim,DecoherencePrelimResource)
admin.site.register(DecoherenceObjectiveQuestion,DecoherenceObjectiveQuestionResource)
admin.site.register(DecoherenceSubjectiveQuestion,DecoherenceSubjectiveQuestionResource)
admin.site.register(ETCRegistration,ETCRegistrationResource)
admin.site.register(VignettoraRegistration,VignettoraRegistrationResource)
admin.site.register(ISCRegistration,ISCRegistrationResource)
admin.site.register(BaseISCRegistration,BaseISCRegistrationResource)
admin.site.register(IBMHackathonRegistration,IBMHackathonRegistrationResource)
admin.site.register(ETCRegisteredRegistration,ETCRegisteredRegistrationResource)
admin.site.register(VignettoraRegisteredRegistration,VignettoraRegisteredRegistrationResource)
admin.site.register(PISRound2Registration,PISRound2RegistrationResource)
admin.site.register(PUBGRegistration,PUBGRegistrationResource)
