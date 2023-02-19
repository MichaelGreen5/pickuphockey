from django.contrib import admin
from pickuphockey.models import Player, Skate, Invitation, GuestList


admin.site.register(Skate)
admin.site.register(Player)
admin.site.register(Invitation)
admin.site.register(GuestList)


# Register your models here.
