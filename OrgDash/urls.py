from django.contrib import admin
from django.urls import path
from OrgDash import views

app_name = 'OrgDash'
urlpatterns = [

path('dashboard/', views.OrganizerDashboard, name = 'organizer_dashboard'),
path('create/new/', views.SkateCreateView.as_view(), name = 'create_event'),
path('dashboard/<int:pk>', views.EventDetail.as_view(), name = 'event_detail'),
path('dashboard/<int:pk>/delete/', views.SkateDeleteView.as_view(), name = 'delete_event'),
path('dashboard/<int:pk>/edit/', views.EventUpdateView.as_view(), name = 'event_update'),
path('dashboard/<int:pk>/guests/', views.guestList, name = 'guest_list'),
path('dashboard/<int:pk>/invite/', views.CreateInvite.as_view(), name = 'create_invite'),
path('dashboard/players/create/', views.CreatePlayer.as_view(), name = 'create_player'),

]