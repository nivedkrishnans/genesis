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
