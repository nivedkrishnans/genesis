from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class UserData(models.Model):
    #associates Author model with User model (Important)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    # additional fields
    event_list = []
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
