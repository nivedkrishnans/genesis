from django.db import models
from django.utils import timezone


class Update(models.Model):
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    publish_date = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Faq(models.Model):
    question= models.TextField()
    answer= models.TextField()
    priority= models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def return_question(self):
        return self.question
    def return_answer(self):
        return self.answer
    def return_priority(self):
        return self.priority
    def __str__(self):
        return self.question
