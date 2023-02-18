from django.contrib import admin
from django.urls import path
from OrgDash import views

app_name = 'OrgDash'
urlpatterns = [

path('dashboard/', views.OrganizerDashboard, name = 'organizer_dashboard'),
path('create/new/', views.SkateCreateView.as_view(), name = 'create_event'),
path('dashboard/<int:pk>', views.EventDash, name = 'event_detail'),
path('dashboard/<int:pk>/manage-invites', views.InviteListView.as_view(), name = 'invite_list'),
path('dashboard/<int:pk>/delete/', views.SkateDeleteView.as_view(), name = 'delete_event'),
path('dashboard/<int:pk>/edit/', views.EventUpdateView.as_view(), name = 'event_update'),
path('dashboard/<int:pk>/teams', views.TeamsView, name = 'make_teams'),
path('dashboard/<int:pk>/invite/', views.CreateInvite.as_view(), name = 'create_invite'),
path('dashboard/players/create/', views.CreatePlayer.as_view(), name = 'create_player'),
path('dashboard/my-players/', views.PlayerListiview.as_view(), name = 'player_list'),
path('dashboard/my-players/<int:pk>', views.PlayerDetail.as_view(), name = 'player_detail'),
path('dashboard/my-players/<int:pk>/edit/', views.PlayerUpdateView.as_view(), name = 'update_player'),
path('dashboard/my-players/<int:pk>/delete/', views.PlayerDeleteView.as_view(), name = 'delete_player'),


]