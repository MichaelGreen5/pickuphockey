from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from OrgDash.models import Skate, Invitation, Player, PlayerGroup, InviteList
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from OrgDash.forms import CreateEventForm, UpdateEventForm, CreateInviteForm, CreatePlayerForm,PlayerUpdateForm, InviteUpdateForm, InviteWaitlistForm, UploadSheetForm,EventRepeatForm
from OrgDash.models import UploadSheet
from django.core.mail import send_mail
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from datetime import timedelta, datetime
from OrgDash.team_sort import SortTeams
import openpyxl






# Create your views here.

def OrganizerDashboard(request):
    today=timezone.now()
    active_user = request.user.pk
    todays_events = Skate.objects.filter(Q(host= active_user) & Q(date=today))
    upcoming_events = Skate.objects.filter(Q(host= active_user) & Q(date__gt= today))
    past_events = Skate.objects.filter(Q(host= active_user) & Q(date__lt= today))
    context = {'upcoming_events' : upcoming_events, 'past_events': past_events, 'todays_events': todays_events}
    return render (request,'OrgDash/dash_base.html',context)

##################SKATES/EVENTS##########################

class SkateCreateView(CreateView):
    template_name = 'OrgDash/Skates/create_event.html'
    success_url = reverse_lazy('OrgDash:organizer_dashboard')
    form_class= CreateEventForm
    model = Skate

    def get_initial(self):
        return {'host': self.request.user}
    
    def get_success_url(self):
            if self.object.recurring_event == True:
                return reverse_lazy('OrgDash:skate_repeat_settings', args=[self.object.pk])
            else:
                return super().get_success_url()


class SkateRepeatUpdate(UpdateView):
    model = Skate
    template_name = 'OrgDash/Skates/skate_repeat_form.html'
    form_class = EventRepeatForm

    def get_success_url(self):
        return reverse('OrgDash:event_detail', args=[self.object.pk])

    
class SkateDeleteView(DeleteView): 
    model = Skate
    template_name = 'OrgDash/confirm_delete.html'
    success_url = reverse_lazy('OrgDash:organizer_dashboard')

    
class EventUpdateView(UpdateView):
    model = Skate
    form_class = UpdateEventForm
    template_name = 'OrgDash/update.html'
    
    def get_success_url(self):
        return reverse('OrgDash:event_detail', args=[self.object.pk])


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
    
    return render (request,'OrgDash/Skates/make_teams.html',context)


def EventDash(request, pk): #TODO waitlist. button to change rsvp to no. Be able to update auto settings.
    active_user = request.user.pk
    active_event = Skate.objects.get(pk=pk)
    all_invited = Invitation.objects.filter(Q(host= active_user) & Q(event=active_event))
    invites_sent = len(all_invited)
    guest_list = Invitation.objects.filter(Q(host= active_user) & Q(event=active_event) & Q(will_you_attend= 'Yes'))
    spots_left = active_event.max_guests - len(guest_list)
    context = {'event': active_event, 'guest_list': guest_list, 'spots_left': spots_left, 'invites_sent':invites_sent}
    return render(request, 'OrgDash/Skates/event_detail.html', context)


##########################INVITATIONS################################


class CreateInvite(CreateView): 
    template_name = 'OrgDash/Invites/create_invite.html'
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


def GuestListView(request,pk):
    active_event = Skate.objects.get(pk=pk)
    event_max_guests = active_event.max_guests 
    active_user = request.user.pk
    all_invited = Invitation.objects.filter(Q(host= active_user) & Q(event=active_event))
    guest_list = Invitation.objects.filter(Q(host= active_user) & Q(event=active_event) & Q(will_you_attend= 'Yes'))
    spots_left = event_max_guests - len(guest_list)
    return render(request, 'OrgDash/Invites/invite_list.html',{'all_invited':all_invited, 'active_event': active_event, 'spots_left': spots_left})


def AddToInviteList(request, pk):
    active_user = request.user.pk
    active_event = Skate.objects.get(pk=pk)
    my_players = Player.objects.filter(created_by=active_user)
    my_groups = PlayerGroup.objects.filter(created_by=active_user)
    existing_invites = Invitation.objects.filter(event=active_event)
    already_invited =[player.guest for player in existing_invites]
    invite_list_tup = InviteList.objects.get_or_create(event= active_event)
    invite_list =invite_list_tup[0].guests.all()
    yet_to_invite = []
    for player in my_players:
        if player not in invite_list:
                yet_to_invite.append(player)
    
    context={
    'active_event':active_event, 'yet_to_invite':yet_to_invite, 
    'my_groups':my_groups, 'invite_list':invite_list, 
    'inv_obj': invite_list_tup[0], 'already_invited': already_invited
    }
    
    if request.method == 'POST':
        form_action = request.POST.get('form_action')
        if form_action == 'add_player':
            selected_player_ids = request.POST.getlist('selected_players_to_add')
            for player_id in selected_player_ids:
     
                invite_list_tup[0].guests.add(player_id)

        elif form_action == 'remove_player':
            selected_player_ids = request.POST.getlist('selected_players_to_remove')
            for player_id in selected_player_ids:
                invite_list_tup[0].guests.remove(player_id)

        else: 
            group_id = request.POST.get('add_group')
            selected_group_members = PlayerGroup.objects.get(id=group_id).members.all()
            for member in selected_group_members:
                invite_list_tup[0].guests.add(member)
         
        return redirect(reverse('OrgDash:add_invites', args=[active_event.pk]), context)
    else:  
        return render(request, 'OrgDash/Invites/add_invites.html', context )


def FinalizeInvites(request, pk): #TODO needs to be unique invite objs only. no duplicates
    invite_list_obj = InviteList.objects.get(pk=pk)
    invite_list = invite_list_obj.guests.all()
    player_emails = [player.email for player in invite_list]
    current_event = invite_list_obj.event
    event_host = current_event.host
    current_user = request.user.pk
    if request.method == 'POST':
        message_field = request.POST.get('inv_message')
        invite_list_obj.message = message_field
        invite_list_obj.create_invites()
        
        subject = "Invitation to " + event_host.first_name + "'s event at " + current_event.location
        from_email = event_host.email
        message = message_field # want this to be link to html template
        recipient_list = player_emails
        # send_mail(subject, message, from_email, recipient_list)
        
        
        return redirect(reverse('OrgDash:event_detail' ,args=[pk]))
    else:
        return render(request, 'OrgDash/Invites/finalize_invites.html', {'inv_obj': invite_list_obj, 'invite_list':invite_list})





# def SendInvites(request,pk): #TODO needs to email invitations DELETE?
#     active_user = request.user.pk
#     active_event = Skate.objects.get(pk=pk)
#     my_players = Player.objects.filter(created_by=active_user)
#     existing_invites = Invitation.objects.filter(event=active_event)
#     my_groups = PlayerGroup.objects.filter(created_by=request.user)
    
    
    
#     existing_guest_emails =[invite.guest.email for invite in existing_invites]
#     players_not_yet_invited =[]    
#     for player in my_players:
#         if player.email not in existing_guest_emails:
#             players_not_yet_invited.append(player)
#     context = {'my_players':my_players, 'event': active_event, 'players_not_yet_invited': players_not_yet_invited, 'existing_invites':existing_invites, 'my_groups':my_groups}
#     if request.method == 'POST':
#         selected_player_ids = request.POST.getlist('selected_players')
        
        
    
#         for player_id in selected_player_ids:
#             player = Player.objects.get(pk=player_id)
#             invite_data = {'host': request.user, 'guest': player,'event': active_event}
#             invite = Invitation(**invite_data)

            
            
            
#             invite.save()
#         return redirect(reverse('OrgDash:event_detail' ,args=[pk]), context)
#     else:
#         return render(request, 'OrgDash/send_invites.html', context)

    
# def InviteGroup(request,slug, pk):
#     current_group = get_object_or_404(PlayerGroup, slug=slug)
#     member_list =current_group.members.all()

#     return render(request, 'OrgDash/invite_group.html', {'current_group':current_group, 'member_list':member_list})


####################PLAYERS##############################


class CreatePlayer(CreateView): 
    template_name = 'OrgDash/Players/create_player.html'
    form_class= CreatePlayerForm
    model = Player
    success_url = reverse_lazy('OrgDash:organizer_dashboard')

    def get_initial(self):
        return {'created_by': self.request.user}

    def get_success_url(self):
        return reverse('OrgDash:player_list')


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

class PlayerDetail(DetailView):
    model = Player
    context_object_name = 'player'
    template_name = 'OrgDash/Players/player_detail.html'


class PlayerListiview(ListView):
    model = Player
    template_name = 'OrgDash/Players/player_list.html'

    def get_queryset(self):
        all_players = super().get_queryset()
        my_players = all_players.filter(created_by = self.request.user)
        return my_players
    

def Playergroups(request):
    active_user = request.user
    my_players = Player.objects.filter(created_by=active_user.pk)
    context={'my_players': my_players }
    if request.method == 'POST':
        selected_player_ids = request.POST.getlist('selected_players')
        group_name = request.POST.get('group_name')
        selected_player_objs = []
        for player_id in selected_player_ids:
            player = Player.objects.get(pk=player_id)
            selected_player_objs.append(player)
        group_data = {'created_by': active_user, 'name':group_name}
        group = PlayerGroup(**group_data)
        group.save()
        group.members.set(selected_player_objs)
        return redirect(reverse('OrgDash:player_group_detail', args= [group.pk]))
    else:

        return render(request, 'OrgDash/Players/create_player_group.html', context)
    
class PlayerGroupDetail(DetailView):
    model= PlayerGroup
    context_object_name = 'group'
    template_name = 'OrgDash/Players/group_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = self.object.members.all()
        return context


class PlayerGroupDelete(DeleteView):
    model = PlayerGroup
    template_name = 'OrgDash/confirm_delete.html'
    success_url = reverse_lazy('OrgDash:player_dash')


def UpdatePlayerGroup(request,pk): 
    active_user = request.user
    my_players = Player.objects.filter(created_by=active_user.pk)
    current_group = PlayerGroup.objects.get(pk=pk)
    members = current_group.members.all()
    member_emails = [member.email for member in members]
    non_members =[]
    for player in my_players:
        if player.email not in member_emails:
            non_members.append(player)

    if request.method == 'POST':
        member_ids = request.POST.getlist('members')
        selected_player_objs =[]
        for id in member_ids:
            member = Player.objects.get(pk=id)
            selected_player_objs.append(member)
        current_group.members.set(selected_player_objs)
        return redirect(reverse('OrgDash:player_group_update', args=[current_group.pk]))

    context={'non_members': non_members, 'members':members, 'current_group': current_group}
    return render(request, 'OrgDash/Players/update_group.html', context)


def PlayerDash(request):
    my_players = Player.objects.filter(created_by=request.user)
    my_groups = PlayerGroup.objects.filter(created_by=request.user)
    return render(request, 'OrgDash/Players/player_dash.html', {'my_groups': my_groups, 'my_players':my_players})


def UploadSheet(request):
    my_players = Player.objects.filter(created_by = request.user)
    player_emails = [player.email for player in my_players]
    if request.method == 'POST':
        form = UploadSheetForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_sheet = form.cleaned_data['file']
            
            wb= openpyxl.load_workbook(uploaded_sheet)
            sheet= wb.active

            max_row=sheet.max_row
            max_column=sheet.max_column
            player_count = 0
            for i in range(2,max_row+1): #assumes first row of sheet has labels, data starts at row 2
                player_row_values = []
                for j in range(1,max_column+1):
                    cell_obj=sheet.cell(row=i,column=j)  
                    player_row_values.append(cell_obj.value)
                
                player_keys = ['first_name', 'last_name', 'email', 'skill']
                player_data = dict(zip(player_keys, player_row_values))
                player_data['created_by']=request.user
                    
                player = Player(**player_data)
                player_count += 1
                if player.email in player_emails:
                    player_count -= 1
                    
                    
                else:
                   player.save()
            messages.success(request, str(player_count) + ' Players added')
            
            
        return redirect('OrgDash:player_dash')
    else:
        form = UploadSheetForm()
        return render(request, 'OrgDash/Players/upload_sheet.html', {'form': form}) 
    














 
    

            
    








    
    