from django.contrib import admin
from .models import *
from import_export.admin import ExportMixin
from django.conf import settings

# Register your models here.

class EventIndexResource(ExportMixin,admin.ModelAdmin):
    fields = ('title','displayTitle','description','priority','startTime','endTime','location','eventLink','coordinatorName','coordinatorContact')    #for showing the fields in this order

    class Meta:
        model = EventIndex

admin.site.register(EventIndex,EventIndexResource)
