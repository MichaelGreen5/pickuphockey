from django.contrib import admin
from OrgDash.models import Player, Skate, Invitation, PlayerGroup, InviteList, Waitlist, LightTeam, DarkTeam, UploadSheet
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from .models import EmailVerification

# UserModel = get_user_model()


# class VerificationInline(admin.StackedInline):
#     model = EmailVerification
#     can_delete = False
#     verbose_name_plural = 'verification'


# class UserAdmin(BaseUserAdmin):
#     inlines = (VerificationInline,)


# admin.site.unregister(UserModel)
# admin.site.register(UserModel, UserAdmin)






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
