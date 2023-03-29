from django.contrib import admin
from OrgDash.models import Player, Skate, Invitation, PlayerGroup, UploadSheet, InviteList, Waitlist, LightTeam, DarkTeam

admin.site.register(Skate)
admin.site.register(Player)
admin.site.register(Invitation)
admin.site.register(UploadSheet)
admin.site.register(PlayerGroup)
admin.site.register(InviteList)
admin.site.register(Waitlist)
admin.site.register(LightTeam)
admin.site.register(DarkTeam)


# Register your models here.
