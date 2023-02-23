from django.shortcuts import render, redirect
from pickuphockey.models import Skate, Invitation, Player
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from OrgDash.forms import CreateEventForm, UpdateEventForm, CreateInviteForm, CreatePlayerForm,PlayerUpdateForm, InviteUpdateForm, InviteWaitlistForm
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from OrgDash.team_sort import SortTeams



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

class SkateDeleteView(DeleteView): 
    model = Skate
    template_name = 'OrgDash/confirm_delete.html'
    success_url = reverse_lazy('OrgDash:organizer_dashboard')

    

class EventUpdateView(UpdateView):
    model = Skate
    form_class = UpdateEventForm
    template_name = 'OrgDash/update.html'
    

    def get_success_url(self):
        return reverse('OrgDash:event_detail', args=[str(self.kwargs['pk'])])


def TeamsView(request, pk): 
    active_user = request.user.pk
    active_event = Skate.objects.get(pk=pk)
    guests = Invitation.objects.filter(Q(host= active_user) & Q(event= active_event) & Q(will_you_attend= 'Yes'))
   
    #Take player skill and make teams
    player_data =[((str(guest.guest), float(guest.guest.skill))) for guest in guests]
    teams = SortTeams(player_data)
    light_team = teams[0]
    light_skill_total = sum([i[1] for i in light_team])
    dark_team = teams[1]
    dark_skill_total = sum([i[1] for i in dark_team])
    context = {'light_team': light_team, 'dark_team': dark_team,
                'light_skill_total' : light_skill_total, 'dark_skill_total': dark_skill_total}
    
    return render (request,'OrgDash/make_teams.html',context)


def EventDash(request, pk): #TODO waitlist. button to change rsvp to no
    active_user = request.user.pk
    active_event = Skate.objects.get(pk=pk)
    all_invited = Invitation.objects.filter(Q(host= active_user) & Q(event=active_event))
    invites_sent = len(all_invited)
    guest_list = Invitation.objects.filter(Q(host= active_user) & Q(event=active_event) & Q(will_you_attend= 'Yes'))
    spots_left = active_event.max_guests - len(guest_list)
    context = {'event': active_event, 'guest_list': guest_list, 'spots_left': spots_left, 'invites_sent':invites_sent}
    return render(request, 'OrgDash/event_detail.html', context)

def SendInvites(request,pk): #TODO needs to email invitations
    active_user = request.user.pk
    active_event = Skate.objects.get(pk=pk)
    my_players = Player.objects.filter(created_by=active_user)
    context = {'my_players':my_players, 'event': active_event}
    if request.method == 'POST':
        selected_player_ids = request.POST.getlist('selected_players')
        number_of_invites = len(selected_player_ids)
    
        for player_id in selected_player_ids:
            player = Player.objects.get(pk=player_id)
            invite_data = {'host': request.user, 'guest': player,'event': active_event}
            invite = Invitation(**invite_data)
            
            
            
            invite.save()
        return redirect(reverse('OrgDash:event_detail' ,args=[pk]), context)
    else:
        return render(request, 'OrgDash/send_invites.html', context)


        


   

    


    






class CreateInvite(CreateView): 
    template_name = 'OrgDash/create_invite.html'
    form_class= CreateInviteForm
    model = Invitation

    def get_form_class(self):
        modelform = super().get_form_class()
        modelform.base_fields['guest'].limit_choices_to = {'created_by': self.request.user}
        return modelform


    def get_success_url(self):
        return reverse('OrgDash:event_detail', args=[str(self.kwargs['pk'])])

    def get_initial(self):
        return {'host': self.request.user, 'event': self.kwargs['pk']}

class CreatePlayer(CreateView): 
    template_name = 'OrgDash/create_player.html'
    form_class= CreatePlayerForm
    model = Player
    success_url = reverse_lazy('OrgDash:organizer_dashboard')
    
    


    def get_initial(self):
        return {'created_by': self.request.user}

    def get_success_url(self):
        return reverse('OrgDash:player_list')

class PlayerListiview(ListView):
    model = Player
    template_name = 'OrgDash/player_list.html'

    def get_queryset(self):
        all_players = super().get_queryset()
        my_players = all_players.filter(created_by = self.request.user)
        return my_players


class PlayerDetail(DetailView):
    model = Player
    context_object_name = 'player'
    template_name = 'OrgDash/player_detail.html'

class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerUpdateForm
    template_name = 'OrgDash/update.html'
    

    def get_success_url(self):
        return reverse('OrgDash:player_detail', args=[str(self.kwargs['pk'])])


class PlayerDeleteView(DeleteView): 
    model = Player
    template_name = 'OrgDash/confirm_delete.html'
    success_url = reverse_lazy('OrgDash:player_list')

def GuestListView(request,pk):
    active_event = Skate.objects.get(pk=pk)
    event_max_guests = active_event.max_guests 
    active_user = request.user.pk
    all_invited = Invitation.objects.filter(Q(host= active_user) & Q(event=active_event))
    guest_list = Invitation.objects.filter(Q(host= active_user) & Q(event=active_event) & Q(will_you_attend= 'Yes'))
    spots_left = event_max_guests - len(guest_list)
    

    return render(request, 'OrgDash/invite_list.html',{'all_invited':all_invited, 'active_event': active_event, 'spots_left': spots_left})

class UpdateInvite(UpdateView):
    model = Invitation
    form_class = InviteUpdateForm
    template_name = 'OrgDash/update.html'

    def get_form_class(self): #TODO do i need to do thes qs again?
        all_invites = super().get_queryset()
        current_event = Invitation.objects.get(pk=self.kwargs['pk'])
        current_host = current_event.event.host
        guest_list = all_invites.filter(Q(host = current_host) & Q(event= current_event.event) & Q(will_you_attend = 'Yes'))

        if len(guest_list) < current_event.event.max_guests:
            
            return InviteUpdateForm
        else:
    
            return InviteWaitlistForm
        
        
    def get_success_url(self):
        current_event = Invitation.objects.get(pk=self.kwargs['pk'])
        event_pk =current_event.event.pk
        return reverse_lazy('OrgDash:invite_list',args = [event_pk])


class DeleteInvite(DeleteView):
    model = Invitation
    template_name = 'OrgDash/confirm_delete.html'

    def get_success_url(self):
        current_event = Invitation.objects.get(pk=self.kwargs['pk'])
        event_pk =current_event.event.pk
        return reverse_lazy('OrgDash:invite_list',args = [event_pk])
    
   
   

   
   
    


    

   

 
    

            
    








    
    