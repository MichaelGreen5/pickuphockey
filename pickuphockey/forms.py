from django import forms
from pickuphockey.models import Skate, Host, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUp(UserCreationForm, forms.Form):
    class Meta:
        fields = ( 'username', 'email','password1', 'password2',)
        model = User


class ProfileForm(forms.ModelForm):
    
    class Meta:
        fields = ('user','is_host',)
        model = Profile

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_host'].label = 'Will you be hosting your own events?'
    



class SkateForm(forms.ModelForm):

    class Meta():
        model = Skate
        fields = ('host', 'time', 'location', 'price',)

        widgets = {
        'time' : forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        

    }

class HostForm(forms.ModelForm):
   class Meta():
        model = Host
        fields = ('user',)