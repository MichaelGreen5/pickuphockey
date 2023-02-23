from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from pickuphockey.models import Skate, Player, Invitation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.db.models import Q
from pickuphockey.forms import SkateForm, SignUp   
from django.urls import reverse_lazy

from django.contrib.auth import login

def baseview(request):
    return render(request, 'base.html')




def skate_details(request, pk): # use some of this to make orgdash
    skate = Skate.objects.get(pk=pk)
    event_id = skate.id
    attending_players =Invitation.objects.filter(Q(will_you_attend= 1) & Q(event= event_id))
    return render(request, 'tonights_skate.html', {'attending_players': attending_players, 'skate': skate})
    

class SkateCreateView(CreateView):
    template_name = 'create_skate.html'
    redirect_field_name = 'pickuphockey/organizer_dashboard.html'
    form_class= SkateForm
    model = Skate
    
   
    









class SignUp(CreateView):
    form_class = SignUp
    success_url = reverse_lazy('create_profile')
    template_name = 'sign_up.html'

    def form_valid(self, form):
        request = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return request 



   



