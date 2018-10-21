from django.contrib import admin
from .models import *
from import_export.admin import ExportMixin
from registration import adminResources

class InOtherWordResource(ExportMixin,admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_staff:
            if request.user.is_superuser:
                return []
            else:
                return ['challengeNo','link_form']
    class Meta:
        model = InOtherWord


class InOtherWordsChallenge01Resource(ExportMixin,admin.ModelAdmin):
    class Meta:
        model = InOtherWordsChallenge01

class InOtherWordsChallenge02Resource(ExportMixin,admin.ModelAdmin):
    class Meta:
        model = InOtherWordsChallenge02

class InOtherWordsChallenge03Resource(ExportMixin,admin.ModelAdmin):
    class Meta:
        model = InOtherWordsChallenge03


class InOtherWordsChallenge04Resource(ExportMixin,admin.ModelAdmin):
    class Meta:
        model = InOtherWordsChallenge04



admin.site.register(ArchiveImage)
admin.site.register(ScienceQuizzine)
admin.site.register(LetsTalkScience)
admin.site.register(InOtherWord,InOtherWordResource)
admin.site.register(InOtherWordsChallenge01,InOtherWordsChallenge01Resource)
admin.site.register(InOtherWordsChallenge02,InOtherWordsChallenge02Resource)
admin.site.register(InOtherWordsChallenge03,InOtherWordsChallenge03Resource)
admin.site.register(InOtherWordsChallenge04,InOtherWordsChallenge04Resource)
