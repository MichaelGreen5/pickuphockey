
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



def SortTeams(player_data):
    player_data.sort(key=get_skill)
    light=[]
    dark=[]
    pick1= player_data.pop()
    pick2= player_data.pop()
    light.append(pick1)
    dark.append(pick2)
    while len(player_data) != 0:
        pick = player_data.pop()
        if WeakTeam(light, dark) == "light":
            light.append(pick)
        else:
            dark.append(pick)

    return light, dark
   






















    
    









  
        






    
    


       



