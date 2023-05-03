from django.contrib import admin
from quickteams.models import QuickBench, QuickDarkTeam, QuickLightTeam, QuickPlayer
# Register your models here.
admin.site.register(QuickBench)
admin.site.register(QuickDarkTeam)
admin.site.register(QuickLightTeam)
admin.site.register(QuickPlayer)