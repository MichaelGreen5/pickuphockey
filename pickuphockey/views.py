from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from pickuphockey.models import Skate, Player, Invitation
from django.db.models import Q
from pickuphockey.forms import SkateForm
from django.urls import reverse_lazy
from pickuphockey.forms import UserSignupForm
from django.contrib.auth import login

def baseview(request):
    return render(request, 'base.html')

def organizer_dashboard(request):
    skate = Skate.objects.filter(host= "James Pijewski") #needs to be whoever is logged in as host
  
    return render (request,'organizer_dashboard.html', {'my_skates' : skate})

def SignUpOptions(request):
    return render(request, "sign_up.html")



def skate_details(request, pk):
    skate = Skate.objects.get(pk=pk)
    event_id = skate.id
    attending_players =Invitation.objects.filter(Q(is_attending= True) & Q(event= event_id))
    return render(request, 'tonights_skate.html', {'attending_players': attending_players, 'skate': skate})
    

class SkateCreateView(CreateView):
    template_name = 'create_skate.html'
    redirect_field_name = 'pickuphockey/organizer_dashboard.html'
    form_class= SkateForm
    model = Skate


    

class PlayerSignUp(CreateView):
    form_class = UserSignupForm
    success_url = reverse_lazy('home')
    template_name = 'sign_up_player.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response 

class SignUpHost(CreateView):
    form_class = UserSignupForm
    success_url = reverse_lazy('organizer_dashboard')
    template_name = 'sign_up_host.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response 


