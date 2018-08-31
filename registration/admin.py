from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.UserData)
admin.site.register(models.AdminEvent)
admin.site.register(models.LasyaRegistration)
