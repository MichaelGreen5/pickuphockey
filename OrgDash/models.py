from django.db import models
from django.core.exceptions import ValidationError
import os
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.utils.text import slugify

from django.urls import reverse



class Player(models.Model):
    first_name = models.CharField(max_length=150, default= None)
    last_name = models.CharField(max_length=150, default= None)
    email = models.EmailField(max_length=150, default= None)
    skill = models.DecimalField(max_digits=4, decimal_places=1)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, default= 1)
    goalie = models.BooleanField(default= False, null= True)
   

    def get_absolute_url(self):
        return reverse('playerlist')

    def player_save(self):
        self.save()

    def __str__(self):
        return (self.first_name + " " + self.last_name)

    class Meta():
        unique_together= ("created_by", "email")



class Skate(models.Model):
    host = models.ForeignKey(User, on_delete= models.CASCADE, default= 1)
    date = models.DateField(auto_now = False, default= None)
    time = models.TimeField(auto_now=False, default= None)
    location = models.CharField(max_length=200)
    price = models.IntegerField()
    max_players = models.IntegerField(default=0)
    max_goalies = models.IntegerField(default=2)
    recurring_event = models.BooleanField(default= False)
    player_full = models.BooleanField(default=False)
    goalie_full = models.BooleanField(default=False)
    STATUS_CHOICES = [
        (7,'Every Week'),
        (14,'Every Two Weeks'),    
    ]
    frequency = models.IntegerField(choices=STATUS_CHOICES, default= 7, blank= True)
    send_invite_days_before = models.IntegerField(default= 3, blank= True)
    finalize_event_hours_before = models.IntegerField(default=1, blank= True)
    group_to_invite = models.ForeignKey('PlayerGroup', on_delete= models.CASCADE, blank= True, null=True)

       

    def get_absolute_url(self): #delete?
        return reverse('OrgDash:organizer_dashboard',kwargs={'slug': (str(self.date) + str(self.time))})
    
    def get_next_skate_info(self):
        added_days = timedelta(days=int(self.frequency))
        next_event_date = self.date + added_days
        next_invite_date = self.send_invites_datetime + added_days
        next_finalize_event_datetime = self.send_invites_datetime + added_days

        return {'host': self.host, 'date': next_event_date, 'time':self.time,'price': self.price, 'location': self.location,
                 'max_guests': self.max_guests, 'recurring_event': self.recurring_event,'frequency': self.frequency,
                   'send_invites_datetime':next_invite_date, 'finalize_event_datetime': next_finalize_event_datetime}
  

    def __str__(self):
        return ("Skate at " + self.location + " "  + str(self.date) + " " + str(self.time))




class Invitation(models.Model):
    host = models.ForeignKey(User, on_delete= models.CASCADE, default= 1)
    guest = models.ForeignKey(Player, on_delete=models.CASCADE)
    event = models.ForeignKey(Skate, on_delete=models.CASCADE)
    date_invited = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('Yes','Yes'),
        ('No','No'),
        ('Waitlist','Put me on the waitlist'),
    ]
    will_you_attend = models.CharField(max_length=256, choices=STATUS_CHOICES, default ='No')
    

    def get_absolute_url(self):
        return reverse('OrgDash:invite_list')

    def __str__(self):
        if self.will_you_attend == 'Yes':
            return self.guest.first_name + " is going to "  + self.event.location 
        else:
            return self.guest.first_name +  " was invited to "  + self.event.location


    class Meta():
        unique_together= ("guest", "event")

class Waitlist(models.Model):
    event = models.ForeignKey(Skate, on_delete=models.CASCADE, blank= True)
    guests = models.ManyToManyField('Player')

    def __str__(self):
        return "Waitlist for " + self.event.location



class PlayerGroup(models.Model):
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, default= 1)
    name = models.CharField(max_length=100, default= "Group Name")
    members = models.ManyToManyField('Player', related_name='groups')
    


    def __str__(self):
        return self.name + " group"


    
    
    
    
    
def validate_sheet_only(value):
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.xlsx', '.xlsm', '.xltx', '.xltm']  # define the valid extensions
    if not ext.lower() in valid_extensions:
        raise ValidationError('File type not supported. Only .xlsx, .xlsm, .xltx, .xltm files are allowed.')

class UploadSheet(models.Model):
    file = models.FileField(upload_to='OrgDash/uploads/', validators=[validate_sheet_only], default= None, null= True)

class InviteList(models.Model):
    event = models.ForeignKey(Skate, on_delete= models.CASCADE)
    guests = models.ManyToManyField('Player')
    message = models.TextField(max_length= 1500, default= "You're Invited!")

    def create_invites(self):
        guest_list = self.guests.all()
        existing_invites = Invitation.objects.filter(event=self.event)
        guests_already_invited =[invite.guest for invite in existing_invites]
        
        for guest in guest_list:
            if guest not in guests_already_invited:
                invite_data = {'host': self.event.host, 'guest': guest,'event': self.event}
                invite = Invitation(**invite_data)
                invite.save()
                

class LightTeam(models.Model):
    event = models.ForeignKey(Skate, on_delete= models.CASCADE, )
    team = models.ManyToManyField('Player')
    skill = models.FloatField(default=0)
   

    def get_total_skill(self):
        light_team_members = self.team.all()
        skill_list = [member.skill for member in light_team_members]
        total_skill = sum(skill_list)
        self.skill = total_skill

class DarkTeam(models.Model):
    event = models.ForeignKey(Skate, on_delete= models.CASCADE, default=1 )
    team = models.ManyToManyField('Player')
    skill = models.FloatField(default=0)
    

    def get_total_skill(self):
        light_team_members = self.team.all()
        skill_list = [member.skill for member in light_team_members]
        total_skill = sum(skill_list)
        self.skill = total_skill

class Bench(models.Model):
    event = models.ForeignKey(Skate, on_delete= models.CASCADE)
    bench_members = models.ManyToManyField('Player')


    def SetBench(self, guests, light_team_obj, dark_team_obj):
        light_team_ids = [player.pk for player in light_team_obj.team.all()]
        dark_team_ids = [player.pk for player in dark_team_obj.team.all()]
        bench = []
        for invite in guests:
            if invite.guest.pk not in light_team_ids:
                if invite.guest.pk not in dark_team_ids:
                    bench.append(invite.guest)
        self.bench_members.set(bench)
    

    

    







