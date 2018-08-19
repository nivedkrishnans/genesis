from django.db import models
from django.utils import timezone


class Update(models.Model):
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    publish_date = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False, blank=True, null=True)
    text = models.TextField()

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
