from django import forms
from pickuphockey.models import Skate

class CreateEventForm(forms.ModelForm):
    class Meta:
        fields = ('host', 'time', 'location', 'price')
        model = Skate

        widgets = {
        'time' : forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }