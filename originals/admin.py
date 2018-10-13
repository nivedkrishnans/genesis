from django.contrib import admin
from .models import ArchiveImage,ScienceQuizzine,LetsTalkScience,InOtherWord,InOtherWordsChallenge01,InOtherWordsChallenge02,InOtherWordsChallenge03
from import_export.admin import ImportExportModelAdmin
from registration import adminResources

class InOtherWordResource(ImportExportModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_staff:
            if request.user.is_superuser:
                return []
            else:
                return ['challengeNo','link_form']
    class Meta:
        model = InOtherWord


class InOtherWordsChallenge01Resource(ImportExportModelAdmin):
    class Meta:
        model = InOtherWordsChallenge01

admin.site.register(ArchiveImage)
admin.site.register(ScienceQuizzine)
admin.site.register(LetsTalkScience)
admin.site.register(InOtherWord)
admin.site.register(InOtherWordsChallenge01)
admin.site.register(InOtherWordsChallenge02)
admin.site.register(InOtherWordsChallenge03)
