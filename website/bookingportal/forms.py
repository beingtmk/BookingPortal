from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EntryForm(forms.Form):

    slots = [('slot1', 'slot1'), ('slot2', 'slot2')]
    fields = [('cricket', 'cricket'), ('badminton', 'badminton'), ('basketball', 'basketball'),]
    #cricket ground, tennis court, badminton court, basketball court, athletic ground, volleyball court, hockey field and football ground

    field_name = forms.ChoiceField(choices=fields)
    date = forms.DateTimeField()
    slot = forms.ChoiceField(choices=slots)
    description = forms.CharField(max_length=500)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    roll_number = forms.IntegerField()
    branch = forms.CharField(max_length=10)
    year = forms.CharField(max_length=10)
    course = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username','password1','first_name', 'last_name', 'email', 'roll_number', 'branch', 'year', 'course',)
