from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model





class Player(models.Model):
    first_name = models.CharField(max_length=150, default= None)
    last_name = models.CharField(max_length=150, default= None)
    email = models.EmailField(max_length=150, default= None)
    skill = models.DecimalField(max_digits=4, decimal_places=1)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, default= 1)

    def get_absolute_url(self):
        return reverse('playerlist')

    def player_save(self):
        self.save()

    def __str__(self):
        return (self.first_name + " " + self.last_name)




class Skate(models.Model):
    host = models.ForeignKey(User, on_delete= models.CASCADE, default= 1)
    date = models.DateField(auto_now = False, default= None)
    time = models.TimeField(auto_now=False, default= None)
    location = models.CharField(max_length=200)
    price = models.IntegerField()
    participants =models.ManyToManyField(Player, through='Invitation', related_name='Player', blank=True)

    def get_absolute_url(self):
        return reverse('OrgDash:organizer_dashboard',kwargs={'slug': (str(self.date) + str(self.time))})

         
  

    
    def __str__(self):
        return ("Skate at " + self.location + " "  + str(self.date) + " " + str(self.time))



class Invitation(models.Model):
    host = models.ForeignKey(User, on_delete= models.CASCADE, default= 1)
    guest = models.ForeignKey(Player, on_delete=models.CASCADE)
    event = models.ForeignKey(Skate, on_delete=models.CASCADE)
    date_invited = models.DateTimeField(auto_now_add=True)
    is_attending = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('OrgDash:invite_list')




    def __str__(self):
        if self.is_attending:
            return self.guest.first_name + " is going to "  + self.event.location 
        else:
            return self.guest.first_name +  " was invited to "  + self.event.location


class GuestList(models.Model):
    event = models.ForeignKey(Skate, on_delete=models.CASCADE)
    guest_list =  models.FilteredRelation('Invitation', condition= models.Q(is_attending = True))









   



