from django.contrib import admin
from django.urls import path
from OrgDash import views

app_name = 'OrgDash'
urlpatterns = [

path('dashboard/', views.OrganizerDashboard, name = 'organizer_dashboard'),
path('create/new/', views.SkateCreateView.as_view(), name = 'create_event'),
path('event/<int:pk>/delete', views.SkateDeleteView.as_view(), name = 'delete_event'),
path('dashboard/<int:pk>', views.EventDetail.as_view(), name = 'event_detail'),

]