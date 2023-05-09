from django.contrib import admin
from django.urls import path
from OrgDash import views

app_name = 'OrgDash'
urlpatterns = [

path('', views.OrganizerDashboard, name = 'organizer_dashboard'),


path('create/new/', views.SkateCreateView.as_view(), name = 'create_event'),
path('<int:pk>', views.EventDash, name = 'event_detail'),
path('<int:pk>/delete/', views.SkateDeleteView.as_view(), name = 'delete_event'),
path('<int:pk>/edit/', views.EventUpdateView.as_view(), name = 'event_update'),
path('<int:pk>/recurring', views.SkateRepeatUpdate.as_view(), name = 'skate_repeat_settings'),
path('<int:pk>/init/recurring', views.InitSkateRepeatUpdate.as_view(), name = 'init_skate_repeat_settings'),
path('<int:pk>/teams', views.TeamsView, name = 'make_teams'),

path('<int:pk>/teams/finalize', views.FinalizeRosters, name = 'finalize_rosters'),



path('<int:pk>/invite/', views.CreateInvite.as_view(), name = 'create_invite'),
# path('<int:pk>/manage-invites', views.GuestListView, name = 'invite_list'),
path('manage-invites/respond/<int:pk>', views.RespondToIinvite, name = 'update_invite'),
path('manage-invites/respond/confirm/<int:pk>/', views.InviteConfirm, name = 'invite_confirm_landing'),
path('<int:pk>/add-invites/', views.AddToInviteList, name='add_invites'),
path('finalize-invites/<int:pk>', views.FinalizeInvites, name = 'finalize_invites'),
path('<int:pk>/manage-invites/delete', views.DeleteInvite.as_view(), name = 'delete_invite'),



path('my-players/', views.PlayerDash, name='player_dash'),
# path('my-players/get-groups', views.GetPlayerGroups, name = 'get_player_groups'),
path('my-players/create/', views.CreatePlayer.as_view(), name = 'create_player'),
path('my-players/<int:pk>', views.PlayerDetail.as_view(), name = 'player_detail'),
path('my-players/<int:pk>/edit/', views.PlayerUpdateView.as_view(), name = 'update_player'),
path('my-players/<int:pk>/delete/', views.PlayerDeleteView.as_view(), name = 'delete_player'),
# path('my-players/list', views.PlayerListiview.as_view(), name = 'player_list'),
path('my-players/upload-sheet', views.UploadSheet, name = 'upload_sheet'),

# path('my-players/goalies/', views.GoalieDash, name = 'goalie_dash'),
# path('my-players/goalies/create', views.CreateGoalie.as_view(), name='create_goalie'),
# path('my-players/goalies/<int:pk>/delete/', views.GoalieDeleteView.as_view(), name = 'delete_goalie'),
# path('my-players/goalies/<int:pk>/edit/', views.GoalieUpdateView.as_view(), name = 'update_goalie'),


# path('my-players/group/<int:pk>', views.PlayerGroupDetail.as_view(), name = 'player_group_detail'),
path('my-players/group/<int:pk>/delete', views.PlayerGroupDelete.as_view(), name = 'player_group_delete'),
path('my-players/new-group', views.Playergroups, name = 'create_player_group'),
path('my-players/group/<int:pk>/edit', views.UpdatePlayerGroup, name= 'player_group_update'),

]