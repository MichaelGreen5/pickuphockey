from django.contrib import admin
from pickuphockey.models import Player, Skate, Invitation
from OrgDash.models import UploadSheet, AutoRecurringSkate

admin.site.register(Skate)
admin.site.register(Player)
admin.site.register(Invitation)
admin.site.register(UploadSheet)
admin.site.register(AutoRecurringSkate)




# Register your models here.
