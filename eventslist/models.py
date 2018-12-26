from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class EventIndex(models.Model):

    title = models.CharField(max_length=200)
    displayTitle = models.CharField(blank=True, null=False, max_length=200)
    description = models.TextField()
    priority = models.IntegerField(default=0)
    startTime=models.DateTimeField( null=True, blank=True)
    endTime=models.DateTimeField( null=True, blank=True)
    location=models.TextField()
    eventLink= models.CharField(max_length=200, default="#")
    coordinatorName=models.CharField(blank=True, null=False, max_length=200)
    coordinatorContact=models.CharField(blank=True, null=False, max_length=200)


    def __str__(self):
        return str(self.title)
