from quickteams.models import QuickPlayer
from django import forms

class CreateQuickPlayer(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateQuickPlayer, self).__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
    class Meta:
        fields = (
            'created_by','name','skill', 'here', 'goalie', 
             )
        model = QuickPlayer




class QuickPlayerUpdateForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'skill', 'here', 'goalie')
        model = QuickPlayer
