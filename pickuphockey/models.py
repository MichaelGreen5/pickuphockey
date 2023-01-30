from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    skill = models.DecimalField(max_digits=4, decimal_places=1)
    RSVP = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('playerlist')

    def player_save(self):
        self.save()

    def __str__(self):
        return (self.user.first_name + " " + self.user.last_name)

  



class Skate(models.Model):
    host = models.CharField(max_length=200, default="James Pijewski")
    time = models.DateTimeField(auto_now=False)
    location = models.CharField(max_length=200)
    price = models.IntegerField()
    participants =models.ManyToManyField(Player, through='Invitation', related_name='events', blank=True, limit_choices_to={'is_attending': True})

    def __str__(self):
        return ("Skate at " + self.location + " hosted by " +self.host )



class Invitation(models.Model):
    guest = models.ForeignKey(Player, on_delete=models.CASCADE)
    event = models.ForeignKey(Skate, on_delete=models.CASCADE)
    date_invited = models.DateTimeField(auto_now_add=True)
    is_attending = models.BooleanField(default=False)

   



