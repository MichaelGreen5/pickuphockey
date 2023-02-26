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

    class Meta():
        unique_together= ("created_by", "email")




class Skate(models.Model):
    host = models.ForeignKey(User, on_delete= models.CASCADE, default= 1)
    date = models.DateField(auto_now = False, default= None)
    time = models.TimeField(auto_now=False, default= None)
    location = models.CharField(max_length=200)
    price = models.IntegerField()
    max_guests = models.IntegerField(default=0)
    

    def get_absolute_url(self):
        return reverse('OrgDash:organizer_dashboard',kwargs={'slug': (str(self.date) + str(self.time))})


    
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



class Group(models.Model):
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, default= 1)
    group_name = models.TextField(max_length= 260)
    players_list = models.ManyToManyField(Player, through='PlayerGroup', default= None)
    

    def __str__(self):
        return self.group_name

class PlayerGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)

    
    














   



