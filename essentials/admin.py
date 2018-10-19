from django.contrib import admin
from .models import Update, Faq
from import_export.admin import ExportMixin

class FaqResource(ExportMixin,admin.ModelAdmin):
    class Meta:
        model = Faq

admin.site.register(Update)
admin.site.register(Faq,FaqResource)
