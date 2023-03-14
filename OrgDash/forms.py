from django import forms
from OrgDash.models import Skate, Invitation, Player, PlayerGroup
from OrgDash.models import UploadSheet
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model

class CreateEventForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
       super(CreateEventForm, self).__init__(*args, **kwargs)
       self.fields['host'].disabled = True
    
    class Meta:
        fields = (
            'host','date', 'time', 'location', 'price', 'max_guests', 
            'recurring_event',  )
        model = Skate

        widgets = {
        'host' : forms.Select(attrs={'class': 'form-control'}),
        'time' : forms.TimeInput(attrs={'type': 'time'}),
        'date' : forms.DateInput(attrs={'type': 'date'}),
        
        
        }
        

class UpdateEventForm(forms.ModelForm):
    class Meta:
        fields = (
            'date', 'time', 'location', 'price', 'max_guests', 'recurring_event',
              )
        model = Skate

        widgets = {
        
        'time' : forms.TimeInput(attrs={'type': 'time'}),
        'date' : forms.DateInput(attrs={'type': 'date'}),
        }

class EventRepeatForm(forms.ModelForm):
    class Meta:
        fields = (
           'frequency', 'group_to_invite', 'send_invite_days_before', 'finalize_event_hours_before'
        )
        model = Skate
        widgets = {
        
        
        }


class CreateInviteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(CreateInviteForm, self).__init__(*args, **kwargs)
       self.fields['host'].disabled = True
       self.fields['event'].disabled = True
       

    class Meta:
        fields = ('host','event', 'guest', 'will_you_attend')
        model = Invitation

class InviteUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        
        super(InviteUpdateForm,self).__init__(*args, **kwargs)
        self.fields['host'].disabled = True
        self.fields['event'].disabled = True
        self.fields['guest'].disabled = True


    
    class Meta:
        fields = ('host','event', 'guest', 'will_you_attend')
        model = Invitation

class InviteWaitlistForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(InviteWaitlistForm,self).__init__(*args, **kwargs)
        self.fields['host'].disabled = True
        self.fields['event'].disabled = True
        self.fields['guest'].disabled = True
        self.fields['will_you_attend'].choices = ('No','No'), ('Waitlist','Put me on the waitlist')
       
        

    class Meta:
        fields = ('host','event', 'guest', 'will_you_attend')
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


class UploadSheetForm(forms.ModelForm):
    class Meta:
        fields= ('file',)
        model = UploadSheet


        
  
        
class UpdatePlayerGroupForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
       
        super(UpdatePlayerGroupForm, self).__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
        
        
    class Meta:
        fields = ('created_by', 'name','members')
        
        model = PlayerGroup
        widgets = {
             
            'members': forms.CheckboxSelectMultiple,
        }
        
        


