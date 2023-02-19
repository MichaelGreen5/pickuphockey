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
       self.fields['event'].disabled = True
       

    class Meta:
        fields = ('host','event', 'guest', 'is_attending',)
        model = Invitation

class InviteUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
       super(InviteUpdateForm,self).__init__(*args, **kwargs)
       self.fields['host'].disabled = True
       self.fields['event'].disabled = True
       self.fields['guest'].disabled = True

    
    class Meta:
        fields = ('host','event', 'guest', 'is_attending')
        model = Invitation

class CreatePlayerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreatePlayerForm, self).__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
    
    class Meta:
        fields = ('created_by', 'first_name','last_name', 'email', 'skill')
        model = Player

class PlayerUpdateForm(forms.ModelForm):
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'skill')
        model = Player

