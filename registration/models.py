from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .customfields import PhoneNumberField,lasya_file_validation,proscenium_file_validation,footprints_file_validation
#from django.db.models.signals import post_save

#def dateUpdate(self):
#    if self.user:
#        self.modified_date = datetime.now()
#    else:
#        self.created_date = datetime.now()

class UserData(models.Model):
    #associates Author model with User model (Important)
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField( null=True, blank=True)
    modify_date = models.DateTimeField( null=True, blank=True)
    # additional fields
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)
    #events Registered
    #lasya = models.BooleanField(default=False)
    #proscenium = models.BooleanField(default=False)
    #footprints = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

class AdminEvent(models.Model):
    REGISTRATION_STATUS_CHOICES=(
        ('notyet','Not Yet'),
        ('opened','Open'),
        ('closed','Closed'),
    )
    registrationStatus = models.CharField(default="notyet", max_length=200, choices=REGISTRATION_STATUS_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    registrationLink = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.title


class LasyaRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(max_length=200)
    teamLeader = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, blank=False)
    contact1 = PhoneNumberField.get_field()
    contact2 = PhoneNumberField.get_field(blank=True)
    participantList =  models.TextField()
    videoFile = models.FileField(validators=[lasya_file_validation], upload_to="fp238a576afovpy23mlzra/do9862x0k3pyl5bxnwxkr8/5n61kixjqfk8lbhkxxvw9m/lasya/%Y/%m/%d", null=True, blank=False)
    def __str__(self):
        return self.teamName

class ProsceniumRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(max_length=200)
    teamLeader = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, blank=False)
    contact1 = PhoneNumberField.get_field()
    contact2 = PhoneNumberField.get_field(blank=True)
    participantList =  models.TextField()
    videoFile = models.FileField(validators=[proscenium_file_validation], upload_to="fp238a576afovpy23mlzra/do9862x0k3pyl5bxnwxkr8/5n61kixjqfk8lbhkxxvw9m/lasya/%Y/%m/%d", null=True, blank=False)
    def __str__(self):
        return self.teamName

class FootprintsRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(max_length=200)
    teamLeader = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, blank=False)
    contact1 = PhoneNumberField.get_field()
    contact2 = PhoneNumberField.get_field(blank=True)
    participantList =  models.TextField()
    videoFile = models.FileField(validators=[footprints_file_validation], upload_to="fp238a576afovpy23mlzra/do9862x0k3pyl5bxnwxkr8/5n61kixjqfk8lbhkxxvw9m/lasya/%Y/%m/%d", null=True, blank=False)
    def __str__(self):
        return self.teamName
