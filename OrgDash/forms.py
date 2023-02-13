from django import forms
from pickuphockey.models import Skate, Invitation, Player

class CreateEventForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
       super(CreateEventForm, self).__init__(*args, **kwargs)
       self.fields['host'].disabled = True
    
    class Meta:
        fields = ('host','date', 'time', 'location', 'price')
        model = Skate

        widgets = {
        'host' : forms.Select(attrs={'class': 'form-control'}),
        'time' : forms.TimeInput(attrs={'type': 'time'}),
        'date' : forms.DateInput(attrs={'type': 'date'}),
        }
        

class UpdateEventForm(forms.ModelForm):
    class Meta:
        fields = ('date', 'time', 'location', 'price')
        model = Skate

        widgets = {
        
        'time' : forms.TimeInput(attrs={'type': 'time'}),
        'date' : forms.DateInput(attrs={'type': 'date'}),
        }

class CreateInviteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(CreateInviteForm, self).__init__(*args, **kwargs)
       self.fields['host'].disabled = True
       

    class Meta:
        fields = ('host','event', 'guest', 'is_attending',)
        model = Invitation

class CreatePlayerForm(forms.ModelForm):
    class Meta:
        fields = ('user', 'skill')
        model = Player


