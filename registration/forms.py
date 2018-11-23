from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from . import models
from .models import *
from django.utils.translation import gettext_lazy as _
from .field_helpers import PhoneNumberField,lasyaSizeLimit,prosceniumSizeLimit,battleofbandsSizeLimit,videoFileSupportMessage,audioVideoFileSupportMessage
from .decoherence_helpers import *

class SignUpForm(forms.Form):
    full_name = forms.CharField(label='Full Name', min_length=3, max_length=127)
    institution = forms.CharField(label='Institution', min_length=3, max_length=127)
    city = forms.CharField(label='City', min_length=3, max_length=127)
    email = forms.EmailField(label='Email')
    contact = forms.CharField(label='Contact number', min_length=3, max_length=20)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class CampusAmbassadorForm(forms.ModelForm):
    class Meta:
        model = CampusAmbassador
        fields = ('full_name', 'institution','city','email','contactForCalls','contactForWhatsapp','howyouknow')
        labels = {
            "full_name": "Full Name",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contactForCalls": "Mobile Number",
            "contactForWhatsapp": "Mobile Number (WhatsApp)",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }

class LasyaForm(forms.ModelForm):
    class Meta:
        model = LasyaRegistration
        fields = ('teamName', 'teamLeader','institution','city','email','contact1','contact2','category','participantList','videoFile','videoFileLink','howyouknow')
        labels = {
            "teamName": "Team Name (Mandatory only for group dance category)",
            "teamLeader": "Team Leader (Mandatory only for group dance category)",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contact1": "Mobile Number",
            "contact2": "Another Mobile Number",
            "category": "Category",
            "participantList": "List of Participants (Enter each participant in a new line or seperated by comma)",
            "videoFile": videoFileSupportMessage(lasyaSizeLimit),
            "videoFileLink":"Link to Video (Only if you do not upload the video file)",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }

class LasyaSoloForm(forms.ModelForm):
    class Meta:
        model = LasyaSoloRegistration
        fields = ('full_name','institution','city','email','contact','videoFile','videoFileLink','howyouknow')
        labels = {
            "full_name" : "Full Name",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contact": "Contact",
            "videoFile": videoFileSupportMessage(lasyaSizeLimit),
            "videoFileLink":"Link to Video (Only if you do not upload the video file)",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }

class LasyaGroupForm(forms.ModelForm):
    class Meta:
        model = LasyaGroupRegistration
        fields = ('teamName', 'teamLeader','institution','city','email','contact1','contact2','participantList','videoFile','videoFileLink','howyouknow')
        labels = {
            "teamName": "Team Name",
            "teamLeader": "Team Leader",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contact1": "Mobile Number",
            "contact2": "Another Mobile Number",
            "participantList": "List of Participants (Enter each participant in a new line or seperated by comma)",
            "videoFile": videoFileSupportMessage(lasyaSizeLimit),
            "videoFileLink":"Link to Video (Only if you do not upload the video file)",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }


class ProsceniumForm(forms.ModelForm):
    class Meta:
        model = ProsceniumRegistration
        fields = ('teamName', 'teamLeader','language','institution','city','email','contact1','contact2','participantList','videoFile','videoFileLink','howyouknow')
        labels = {
            "teamName": "Team Name",
            "teamLeader": "Team Leader",
            "language":"Language",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contact1": "Mobile Number",
            "contact2": "Another Mobile Number",
            "participantList": "List of Participants (Enter each participant in a new line or seperated by comma)",
            "videoFile": videoFileSupportMessage(prosceniumSizeLimit),
            "videoFileLink":"Link to Video (Only if you do not upload the video file)",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }


class BattleOfBandsForm(forms.ModelForm):
    class Meta:
        model = BattleOfBandsRegistration
        fields = ('teamName', 'teamLeader','institution','city','regionalfinalscity','email','contact1','contact2','participantList','audioVideoFile','audioVideoFileLink','howyouknow')
        labels = {
            "teamName": "Team Name",
            "teamLeader": "Team Leader",
            "institution": "Institution (If not applicable, feel free to amuse us!)",
            "city": "City",
            "regionalfinalscity": "Regional Finals City Preference",
            "email": "Email",
            "contact1": "Mobile Number",
            "contact2": "Another Mobile Number",
            "participantList": "List of Participants (Enter each participant in a new line or seperated by comma)",
            "audioVideoFile": audioVideoFileSupportMessage(battleofbandsSizeLimit),
            "audioVideoFileLink": "Link to Audio/Video (Only if you do not upload the file)",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }

class FootprintsForm(forms.ModelForm):
    class Meta:
        model = FootprintsRegistration
        fields = ('teamName', 'teamLeader','language','institution','city','email','contact1','contact2','participantList','howyouknow')
        labels = {
            "teamName": "Team Name",
            "teamLeader": "Team Leader",
            "language":"Language",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contact1": "Mobile Number",
            "contact2": "Another Mobile Number",
            "participantList": "List of Participants (Enter each participant in a new line or seperated by comma)",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }

class DecoherenceForm(forms.ModelForm):
    class Meta:
        model = DecoherenceRegistration
        fields = ('teamName', 'institution','city', 'participant1', 'qualification1', 'email1', 'contact1', 'participant2', 'qualification2', 'email2', 'contact2','howyouknow')
        labels = {
            "teamName": "Team Name",
            "institution": "Institution",
            "participant1": "Full Name",
            "qualification1": "Qualification",
            "email1": 'Email',
            "contact1": "Mobile Number",
            "participant2": "Full Name",
            "qualification2": "Qualification",
            "email2": 'Email',
            "contact2": "Mobile Number",
            "city": "City",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }

class ChemisticonForm(forms.ModelForm):
    class Meta:
        model = ChemisticonRegistration
        fields = ('teamName', 'institution','city', 'participant1', 'qualification1', 'email1', 'contact1',
        'participant2', 'qualification2', 'email2', 'contact2',
        'participant3', 'qualification3', 'email3', 'contact3','howyouknow')
        labels = {
            "teamName": "Team Name",
            "institution": "Institution",
            "participant1": "Full Name",
            "qualification1": "Qualification",
            "email1": 'Email',
            "contact1": "Mobile Number",
            "participant2": "Full Name",
            "qualification2": "Qualification",
            "email2": 'Email',
            "contact2": "Mobile Number",
            "participant3": "Full Name",
            "qualification3": "Qualification",
            "email3": 'Email',
            "contact3": "Mobile Number",
            "city": "City",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }

class DebubularyForm(forms.ModelForm):
    class Meta:
        model = DebubularyRegistration
        fields = ('teamName', 'institution','city', 'participant1', 'email1', 'contact1', 'participant2', 'email2', 'contact2','howyouknow')
        labels = {
            "teamName": "Team Name",
            "institution": "Institution",
            "participant1": "Full Name",
            "email1": 'Email',
            "contact1": "Mobile Number",
            "participant2": "Full Name",
            "email2": 'Email',
            "contact2": "Mobile Number",
            "city": "City",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }

class CryptothlonForm(forms.ModelForm):
    class Meta:
        model = CryptothlonRegistration
        fields = ('teamName', 'institution','city', 'participant1', 'email1', 'contact1', 'participant2', 'email2', 'contact2','howyouknow')
        labels = {
            "teamName": "Team Name",
            "institution": "Institution",
            "participant1": "Full Name",
            "email1": 'Email',
            "contact1": "Mobile Number",
            "participant2": "Full Name",
            "email2": 'Email',
            "contact2": "Mobile Number",
            "city": "City",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }

class WikimediaPhotographyForm(forms.ModelForm):
    class Meta:
        model = WikimediaPhotographyRegistration
        fields = ('wikimediaUsername', 'submission1','submission2','submission3','submission4','submission5','howyouknow')
        labels = {
            "wikimediaUsername": "Wikimedia Username",
            "submission1": "Submission Link 1",
            "submission2": "Submission Link 2 (Optional)",
            "submission3": "Submission Link 3 (Optional)",
            "submission4": "Submission Link 4 (Optional)",
            "submission5": "Submission Link 5 (Optional)",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }

class VignettoraForm(forms.ModelForm):
    class Meta:
        model = VignettoraRegistration
        fields = ('full_name','institution','city','email','contact','howyouknow')
        labels = {
            "full_name": "Full Name",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contact": "Mobile Number",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"

        }

class ETCForm(forms.ModelForm):
    class Meta:
        model = ETCRegistration
        fields = ('full_name','year','major','institution','city','email','contact',
        'physics','mathematics','chemistry','biology','psychology','economics','other_subjects','topic','howyouknow')
        labels = {
            "full_name":"Full Name",
            "year":"Year in School/College",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contact": "Mobile Number",
            "physics":"Physics",
            "mathematics":"Mathematics",
            "chemistry":"Chemistry",
            "biology":"Biology",
            "psychology":"Psychology",
            "economics":"Economics",
            'other_subjects': 'Others (optional)',
            "topic":"Briefly describe your tentative ideas/choice of topic/general field you will pick from",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
        }

class PISForm(forms.ModelForm):
    class Meta:
        model = PISRegistration
        fields = ('teamName', 'member1name','member1mobile','member1email','member2name','member2mobile','member2email','member3name','member3mobile','member3email','ideaAbstract','motivation','prospects','marketResearch','prototyping','howyouknow')
        labels = {
            "teamName": "Team Name",
            "member1name": "Name",
            "member1mobile": "Mobile Number",
            "member1email": "Email",
            "member2name": "Name",
            "member2mobile": "Mobile Number",
            "member2email": "Email",
            "member3name": "Name",
            "member3mobile": "Mobile Number",
            "member3email": "Email",
            "ideaAbstract": "Tell us about your idea (Max 250 words)",
            "motivation": "Tell us why you want to do this. What motivates you? (Max 500 words)",
            "prospects": "How do you think your idea will make an impact?",
            "marketResearch": "Market Research (Target customers, potential sposors) (optional)",
            "prototyping": "Prototyping (Product feasibility, scalability, and current progress) (optional)",
            "howyouknow": "How did you come to know about this event/program? (Eg: Name/ID of Campus Ambassador, Facebook, Instagram, etc.)"
            }

class DecoherencePrelimsForm(forms.ModelForm):
    class Meta:
        model = DecoherencePrelim
        fields = ('question01', 'question02', 'question03', 'question04', 'question05', 'question06', 'question07', 'question08', 'question09', 'question10', 'question11', 'question12', 'question13', 'question14', 'question15', 'question16', 'question17', 'question18', 'question19', 'question20', 'question21', 'question22', 'question23', 'question24', 'question25','subjectiveAnswers')
        labels = {
            'question01':getDecoherenceObjectiveQuestions(1),
            'question02':getDecoherenceObjectiveQuestions(2),
            'question03':getDecoherenceObjectiveQuestions(3),
            'question04':getDecoherenceObjectiveQuestions(4),
            'question05':getDecoherenceObjectiveQuestions(5),
            'question06':getDecoherenceObjectiveQuestions(6),
            'question07':getDecoherenceObjectiveQuestions(7),
            'question08':getDecoherenceObjectiveQuestions(8),
            'question09':getDecoherenceObjectiveQuestions(9),
            'question10':getDecoherenceObjectiveQuestions(10),
            'question11':getDecoherenceObjectiveQuestions(11),
            'question12':getDecoherenceObjectiveQuestions(12),
            'question13':getDecoherenceObjectiveQuestions(13),
            'question14':getDecoherenceObjectiveQuestions(14),
            'question15':getDecoherenceObjectiveQuestions(15),
            'question16':getDecoherenceObjectiveQuestions(16),
            'question17':getDecoherenceObjectiveQuestions(17),
            'question18':getDecoherenceObjectiveQuestions(18),
            'question19':getDecoherenceObjectiveQuestions(19),
            'question20':getDecoherenceObjectiveQuestions(20),
            'question21':getDecoherenceObjectiveQuestions(21),
            'question22':getDecoherenceObjectiveQuestions(22),
            'question23':getDecoherenceObjectiveQuestions(23),
            'question24':getDecoherenceObjectiveQuestions(24),
            'question25':getDecoherenceObjectiveQuestions(25),
            'subjectiveAnswers': "Upload answers for the subjective questions (single file, PDF or ZIP only)",
        }
        widgets = {
            'question01':forms.RadioSelect(attrs={'class':'radioS'}),
            'question02':forms.RadioSelect(attrs={'class':'radioS'}),
            'question03':forms.RadioSelect(attrs={'class':'radioS'}),
            'question04':forms.RadioSelect(attrs={'class':'radioS'}),
            'question05':forms.RadioSelect(attrs={'class':'radioS'}),
            'question06':forms.RadioSelect(attrs={'class':'radioS'}),
            'question07':forms.RadioSelect(attrs={'class':'radioS'}),
            'question08':forms.RadioSelect(attrs={'class':'radioS'}),
            'question09':forms.RadioSelect(attrs={'class':'radioS'}),
            'question10':forms.RadioSelect(attrs={'class':'radioS'}),
            'question11':forms.RadioSelect(attrs={'class':'radioS'}),
            'question12':forms.RadioSelect(attrs={'class':'radioS'}),
            'question13':forms.RadioSelect(attrs={'class':'radioS'}),
            'question14':forms.RadioSelect(attrs={'class':'radioS'}),
            'question15':forms.RadioSelect(attrs={'class':'radioS'}),
            'question16':forms.RadioSelect(attrs={'class':'radioS'}),
            'question17':forms.RadioSelect(attrs={'class':'radioS'}),
            'question18':forms.RadioSelect(attrs={'class':'radioS'}),
            'question19':forms.RadioSelect(attrs={'class':'radioS'}),
            'question20':forms.RadioSelect(attrs={'class':'radioS'}),
            'question21':forms.RadioSelect(attrs={'class':'radioS'}),
            'question22':forms.RadioSelect(attrs={'class':'radioS'}),
            'question23':forms.RadioSelect(attrs={'class':'radioS'}),
            'question24':forms.RadioSelect(attrs={'class':'radioS'}),
            'question25':forms.RadioSelect(attrs={'class':'radioS'}),
        }
