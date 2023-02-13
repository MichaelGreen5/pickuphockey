from django.shortcuts import render, redirect
from pickuphockey.models import Skate, Invitation, Player
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from OrgDash.forms import CreateEventForm, UpdateEventForm, CreateInviteForm, CreatePlayerForm
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.utils import timezone




# Create your views here.

def OrganizerDashboard(request):
    today=timezone.now()
    active_user = request.user.pk
    todays_events = Skate.objects.filter(Q(host= active_user) & Q(date=today))
    upcoming_events = Skate.objects.filter(Q(host= active_user) & Q(date__gt= today))
    past_events = Skate.objects.filter(Q(host= active_user) & Q(date__lt= today))
    context = {'upcoming_events' : upcoming_events, 'past_events': past_events, 'todays_events': todays_events}
   

    return render (request,'OrgDash/dash_base.html',context)

class SkateCreateView(CreateView):
    template_name = 'OrgDash/create_event.html'
    success_url = reverse_lazy('OrgDash:organizer_dashboard')
    form_class= CreateEventForm
    model = Skate

    def get_initial(self):
        return {'host': self.request.user}

class SkateDeleteView(DeleteView): #TODO make detail view, then give option to edit or delete inside detail view
    model = Skate
    template_name = 'OrgDash/confirm_delete.html'
    success_url = reverse_lazy('OrgDash:organizer_dashboard')

    


class EventDetail(DetailView):
    model = Skate
    context_object_name = 'event'
    template_name = 'OrgDash/event_detail.html'




class EventUpdateView(UpdateView):
    model = Skate
    form_class = UpdateEventForm
    template_name = 'OrgDash/update_event.html'
    

    def get_success_url(self):
        return reverse('OrgDash:event_detail', args=[str(self.kwargs['pk'])])


def guestList(request, pk):
    active_user = request.user.pk
    active_event = Skate.objects.get(pk=pk)
    guests = Invitation.objects.filter(Q(host= active_user) & Q(event= active_event) & Q(is_attending= True))
    return render (request,'OrgDash/guest_list.html',{'guests':guests})

class CreateInvite(CreateView):
    template_name = 'OrgDash/create_invite.html'
    form_class= CreateInviteForm
    model = Invitation

    def get_success_url(self):
        return reverse('OrgDash:event_detail', args=[str(self.kwargs['pk'])])

    def get_initial(self):
        return {'host': self.request.user}

class CreatePlayer(CreateView): #TODO player list. Need to have "my players" grouped by host. do they all need to be users?
    template_name = 'OrgDash/create_player.html'
    form_class= CreatePlayerForm
    model = Player
    success_url = reverse_lazy('OrgDash:organizer_dashboard')







    
    