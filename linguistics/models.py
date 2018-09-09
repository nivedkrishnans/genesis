from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator



class challenge1response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(max_length=200)
    teamLeader = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, blank=False)
    participantList =  models.TextField()
    videoFile = models.FileField( upload_to="fp238a576afovpy23mlzra/do9862x0k3pyl5bxnwxkr8/5n61kixjqfk8lbhkxxvw9m/lasya/%Y/%m/%d", null=True, blank=False)
    def __str__(self):
        return self.teamName
