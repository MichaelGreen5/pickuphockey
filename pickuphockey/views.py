from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from pickuphockey.models import Skate, Player, Invitation
from django.db.models import Q

# Create your views here.
def baseview(request):
    return render(request, 'base.html')


class SkateListView(ListView):
    model = Invitation
    template_name = 'tonights_skate.html'
    
    def get_queryset(self):
        return Invitation.objects.filter(is_attending= True)

def skate_details(request, pk):
    skate = Skate.objects.get(pk=pk)
    event_id = skate.id
    
    
    
   

    attending_players =Invitation.objects.filter(Q(is_attending= True) & Q(event= event_id))
   
   
    
    return render(request, 'tonights_skate.html', {'attending_players': attending_players, 'skate': skate})
    




