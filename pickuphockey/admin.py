from django.contrib import admin
from pickuphockey.models import Player, Skate, Invitation, Profile


admin.site.register(Skate)
admin.site.register(Player)
admin.site.register(Invitation)
admin.site.register(Profile)

# Register your models here.
