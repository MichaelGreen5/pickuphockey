from OrgDash.models import LightTeam, DarkTeam, Bench

def WeakTeam(light, dark):
    light_skill = 0
    for i in light:
        light_skill += i[1]
    
    dark_skill = 0
    for i in dark:
        dark_skill += i[1]
    
    if light_skill < dark_skill:
        return 'light'
    else:
        return 'dark'


def get_skill(player):
    return player[1]



def SortTeams(player_data, goalie_data):
    player_data.sort(key=get_skill)
    goalie_data.sort(key=get_skill)
    light=[]
    dark=[]
    pick1= player_data.pop()
    pick2= player_data.pop()
    light.append(pick1)
    dark.append(pick2)
    while len(player_data) != 0:
        pick = player_data.pop()
        if WeakTeam(light, dark) == 'light':
            light.append(pick)
        else:
            dark.append(pick)
    while len(goalie_data) != 0:
        goalie_pick = goalie_data.pop()
        if WeakTeam(light, dark) == 'light':
            light.append(goalie_pick)
        else:
            dark.append(goalie_pick)
    return light, dark





def SetTeams(teams, active_event):
    # set light team
    light_team_members = [player[0] for player in teams[0]]
    light_team_tup = LightTeam.objects.get_or_create(event=active_event)
    light_team_obj = light_team_tup[0]
    light_team_obj.team.set(light_team_members)

    
    # set dark team
    dark_team_members = [player[0] for player in teams[1]]
    dark_team_tup = DarkTeam.objects.get_or_create(event=active_event)
    dark_team_obj = dark_team_tup[0]
    dark_team_obj.team.set(dark_team_members)
  



def AddToTeam(team_obj, selected_player_ids):
    for player_id in selected_player_ids:
        team_obj.team.add(player_id)
    
    
    


def RemoveFromTeam(team_obj, selected_player_ids):
    for player_id in selected_player_ids:
        team_obj.team.remove(player_id)
    
    







    
   





   






















    
    









  
        






    
    


       



