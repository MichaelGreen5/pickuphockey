from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model




class Profile(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_host = models.BooleanField(default= False)

    def __str__(self):
        return self.user.username

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    skill = models.DecimalField(max_digits=4, decimal_places=1)

    def get_absolute_url(self):
        return reverse('playerlist')

    def player_save(self):
        self.save()

    def __str__(self):
        return (self.user.username)

  
class Host(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.user.first_name + ", host account"



class Skate(models.Model):
    host = models.ManyToManyField(User)
    time = models.DateTimeField(auto_now=False)
    location = models.CharField(max_length=200)
    price = models.IntegerField()
    participants =models.ManyToManyField(Player, through='Invitation', related_name='Player', blank=True)

    def get_absolute_url(self):
        return reverse('OrgDash/organizer_dashboard')
  

    
    def __str__(self):
        return ("Skate at " + self.location )



class Invitation(models.Model):
    guest = models.ForeignKey(Player, on_delete=models.CASCADE)
    event = models.ForeignKey(Skate, on_delete=models.CASCADE)
    date_invited = models.DateTimeField(auto_now_add=True)
    is_attending = models.BooleanField(default=False)

    def __str__(self):
        if self.is_attending:
            return self.guest.user.first_name + " " + self.guest.user.last_name + " is going to " + self.event.location
        else:
            return self.guest.user.first_name + " " + self.guest.user.last_name + " was invited to " + self.event.location



class GuestList(models.Model):
    if Invitation.is_attending == True:
        particapants = Invitation.guest.field.name

    guests = models.ManyToManyField(Invitation) 


   



