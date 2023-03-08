from django.contrib import admin
from pickuphockey.models import Player, Skate, Invitation, PlayerGroup
from OrgDash.models import UploadSheet

admin.site.register(Skate)
admin.site.register(Player)
admin.site.register(Invitation)
admin.site.register(UploadSheet)
admin.site.register(PlayerGroup)




# Register your models here.
