from django import forms
from django.core.exceptions import ValidationError
from . import models
from .models import *
from django.utils.translation import gettext_lazy as _

class InOtherWordsChallengeForm01(forms.ModelForm):
    class Meta:
        model = InOtherWordsChallenge01
        fields = ('city01','city02','city03','city04','city05','city06','city07','city08','city09','city10','bonusquestion',)
        labels = {
			"city01": "City Number 1",
			"city02": "City Number 2",
			"city03": "City Number 3",
			"city04": "City Number 4",
			"city05": "City Number 5",
			"city06": "City Number 6",
			"city07": "City Number 7",
			"city08": "City Number 8",
			"city09": "City Number 9",
			"city10": "City Number 10",
			"bonusquestion": "Bonus Question",
        }


class InOtherWordsChallengeForm02(forms.ModelForm):
    class Meta:
        model = InOtherWordsChallenge02
        fields = ('placesOrder','question2',)
        labels = {
			"placesOrder": "Order of the five places",
			"question2": "Answer to Question 2",
        }


class InOtherWordsChallengeForm03(forms.ModelForm):
    class Meta:
        model = InOtherWordsChallenge03
        fields = ('question1','question2a','question2b','question2c','question2d','question2e',)
        labels = {
			"question1": "Question 1",
			"question2a": "Question 2(a)",
			"question2b": "Question 2(b)",
			"question2c": "Question 2(c)",
			"question2d": "Question 2(d)",
			"question2e": "Question 2(e)",
        }



class InOtherWordsChallengeForm04(forms.ModelForm):
    class Meta:
        model = InOtherWordsChallenge04
        fields = ('question1','question2','question3','question4','question5',)
        labels = {
			"question1": "Question 1",
			"question2": "Question 2",
			"question3": "Question 3",
			"question4": "Question 4",
			"question5": "Question 5",
        }


class InOtherWordsChallengeForm05(forms.ModelForm):
    class Meta:
        model = InOtherWordsChallenge05
        fields = ('question1','question2','question3','question4','question5','question6','question7','question8','question9','question10','question11','question12','question13','question14','question15',)
        labels = {
			"question1": "1",
			"question2": "2",
			"question3": "3",
			"question4": "4",
			"question5": "5",
            "question6": "6",
			"question7": "7",
			"question8": "8",
			"question9": "9",
			"question10": "10",
            "question11": "11",
			"question12": "12",
			"question13": "13",
			"question14": "14",
			"question15": "15",
        }
