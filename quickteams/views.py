from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from quickteams.models import QuickBench, QuickDarkTeam, QuickLightTeam, QuickPlayer
from OrgDash.models import Player
from django.views.generic import CreateView, UpdateView, DeleteView
from quickteams.forms import CreateQuickPlayer, QuickPlayerUpdateForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class CreatePlayer(LoginRequiredMixin, CreateView): 
    template_name = 'quickteams/create_quick_player.html'
    form_class= CreateQuickPlayer
    model = Player
    success_url = reverse_lazy('quickteams:quick_teams')

    def get_initial(self):
        return {'created_by': self.request.user}
    
class EditQuickPlayer(LoginRequiredMixin, UpdateView):
    template_name = 'quickteams/update_quick_player.html'
    form_class = QuickPlayerUpdateForm
    model = QuickPlayer
    success_url = reverse_lazy('quickteams:quick_teams')

class DeleteQuickPlayer(LoginRequiredMixin, DeleteView): 
    model = QuickPlayer
    template_name = 'OrgDash/confirm_delete.html'
    success_url = reverse_lazy('quickteams:quick_teams')

    





@login_required 
def QuickTeams(request):
    
    from OrgDash.team_sort import SortTeams
    active_user = request.user
    my_players = QuickPlayer.objects.filter(created_by=active_user)
    skaters = []
    goalies = []
    
    for player in my_players:
        if player.goalie & player.here:
            goalies.append(player)
        elif player.here:
            skaters.append(player)
    num_players_here = len(skaters) + len(goalies)
    
    #Take player skill from player objs
    player_data =[((player), float(player.skill)) for player in skaters]
    goalie_data = [((player), float(player.skill)) for player in goalies]
    # get light obj
    quick_light_obj, created = QuickLightTeam.objects.get_or_create(created_by=active_user)
    if created:
        quick_light_obj.created_by = active_user
        quick_light_obj.save()
    #  = light_team_tup[0]
    quick_light_obj.get_total_skill()
    
    #get dark obj
    quick_dark_obj, created = QuickDarkTeam.objects.get_or_create(created_by=active_user)
    if created:
        quick_dark_obj.created_by = active_user
        quick_dark_obj.save()
    
    #  = dark_team_tup[0]
    quick_dark_obj.get_total_skill()
    
    # get bench
    quick_bench_obj, created = QuickBench.objects.get_or_create(created_by= active_user)
    if created:
        quick_bench_obj.created_by = active_user
        quick_bench_obj.save()
    
   
    
    total_skill = (float(quick_dark_obj.skill) + float(quick_light_obj.skill))
    
    context = {'light_team': quick_light_obj.team.all(), 'dark_team': quick_dark_obj.team.all(), 'total_skill':total_skill, 'my_players':my_players,
                'light_team_skill' : quick_light_obj.skill, 'dark_team_skill': quick_dark_obj.skill, 'bench_members': quick_bench_obj.bench_members.all(),
                'num_players_here': num_players_here}
    if request.method == 'POST':
        here_action = request.POST.get('here_form_action')
        sort_action = request.POST.get('auto_sort')
        clear_action = request.POST.get('clear_teams')
        
        if here_action == 'confirm_here':
            whos_here = request.POST.getlist('here_player')
            
            for player in my_players:
                if str(player.pk) in whos_here:
                    player.here = True
                    
                else:
                    player.here = False
                player.save()
            

       
        if sort_action == 'auto_sort':
            teams = SortTeams(player_data, goalie_data)
            
            # set light teams
            light_team_members = [player[0] for player in teams[0]]
            quick_light_obj.team.set(light_team_members)

            # set dark team
            dark_team_members = [player[0] for player in teams[1]]
            quick_dark_obj.team.set(dark_team_members)

        if clear_action == 'clear_teams':
            quick_light_obj.team.clear()
            quick_dark_obj.team.clear()

        return redirect(reverse('quickteams:quick_teams' ),context)
    else:
        return render (request,'quickteams/quick_teams.html',context)
