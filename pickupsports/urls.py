"""pickupsports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pickuphockey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.baseview, name = 'home'),
    path('tonight/<int:pk>/', views.skate_details, name='tonights_skate'),
    path('host/', views.organizer_dashboard, name = 'organizer_dashboard'),
    path('host/create/skate', views.SkateCreateView.as_view(), name = 'create_skate'),
    path('signup/', views.SignUpOptions, name = 'sign_up_options'),
    path('signup/guest', views.PlayerSignUp.as_view(), name = 'player_sign_up'),
    path('signup/host', views.SignUpHost.as_view(), name = 'host_sign_up')
 
    

]
