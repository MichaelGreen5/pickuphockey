from django.db import models

from django.contrib.auth.models import User

class QuickPlayer(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=300, default=None)
    skill = models.DecimalField(max_digits=4, decimal_places=1)
    here = models.BooleanField(default= False, null= True)
    goalie = models.BooleanField(default= False, null= True)

    def __str__(self):
        return self.name
    
class QuickLightTeam(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    team = models.ManyToManyField(QuickPlayer)
    skill = models.FloatField(default=0)
   

    def get_total_skill(self):
        light_team_members = self.team.all()
        skill_list = [member.skill for member in light_team_members]
        total_skill = sum(skill_list)
        self.skill = total_skill

class QuickDarkTeam(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    team = models.ManyToManyField(QuickPlayer)
    skill = models.FloatField(default=0)
    

    def get_total_skill(self):
        light_team_members = self.team.all()
        skill_list = [member.skill for member in light_team_members]
        total_skill = sum(skill_list)
        self.skill = total_skill

class QuickBench(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    bench_members = models.ManyToManyField(QuickPlayer)


    def SetBench(self, my_players, light_team_obj, dark_team_obj):
        light_team_ids = [player.pk for player in light_team_obj.team.all()]
        dark_team_ids = [player.pk for player in dark_team_obj.team.all()]
        bench = []
        for player in my_players:
            if player.pk not in light_team_ids:
                if player.pk not in dark_team_ids:
                    bench.append(player)
        self.bench_members.set(bench)
    
