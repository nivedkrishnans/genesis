from django.db import models
from django import forms
from django.utils import timezone
from .models import *


def getDecoherenceObjectiveOptions(n):
    options = ['A','B','C','D','(Skip)']
    try:
        thisQuestion = list(DecoherenceObjectiveQuestion.objects.filter(qNo=n))[0]
        options=[thisQuestion.choice1,thisQuestion.choice2,thisQuestion.choice3,thisQuestion.choice4, '(Skip)']
    except:
        options = ['A','B','C','D','(Skip)']
    CHOICES=(
        ('A',options[0]),
        ('B',options[1]),
        ('C',options[2]),
        ('D',options[3]),
        ('S',options[4]),
    )
    return CHOICES

def getDecoherenceObjectiveQuestions(n):
    questionText = "Question " + str(n)
    try:
        thisQuestion = list(DecoherenceObjectiveQuestion.objects.filter(qNo=n))[0]
        questionText = thisQuestion.text
    except:
        questionText = "Question " + str(n)
    return questionText


def getDecoherenceSubjectiveQuestions(n):
    questionText = "Question " + str(n)
    try:
        thisQuestion = list(DecoherenceSubjectiveQuestion.objects.filter(qNo=n))[0]
        questionText = thisQuestion.text
    except:
        questionText = "Question " + str(n)
    return questionText
