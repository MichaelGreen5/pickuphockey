from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# User = get_user_model()

class SignUp(UserCreationForm, forms.Form):
    class Meta:
        fields = ( 'username', 'email','password1', 'password2',)
        model = User

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  



class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        UserModel = get_user_model()
        if not UserModel.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError(("There is no user registered with the specified email address!"))
        return email









    


            