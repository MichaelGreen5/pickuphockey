from django.contrib import admin
from django.urls import path
from quickteams import views

app_name = 'quickteams'
urlpatterns = [

path('', views.QuickTeams, name='quick_teams'),
path('create-player', views.CreatePlayer.as_view(), name = 'create_quick_player'),
path('edit-player/<int:pk>', views.EditQuickPlayer.as_view(), name = 'update_quick__player'),
path('delete-player/<int:pk>', views.DeleteQuickPlayer.as_view(), name = 'delete_quick_player'),

]