from django import forms
from pickuphockey.models import Skate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUp(UserCreationForm, forms.Form):
    class Meta:
        fields = ( 'username', 'email','password1', 'password2',)
        model = User


    

user = get_user_model()

class SkateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(SkateForm, self).__init__(*args, **kwargs)
       self.fields['host'].disabled = True
    
   

    class Meta():
        model = Skate
        fields = ('host', 'time', 'location', 'price',)

        widgets = {
        'host' : forms.Select(attrs={'class': 'form-control'}),
        'time' : forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        

    }
    


            