from django import forms
from pickuphockey.models import Skate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserSignupForm(UserCreationForm, forms.ModelForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2',)
        model = User


class SkateForm(forms.ModelForm):

    class Meta():
        model = Skate
        fields = ('host', 'time', 'location', 'price',)

        widgets = {
        'time' : forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        

    }