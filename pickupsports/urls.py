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
from django.urls import path, include
from pickuphockey import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.baseview, name = 'home'),
    path('tonight/<int:pk>/', views.skate_details, name='tonights_skate'),
   
    path('host/create/skate', views.SkateCreateView.as_view(), name = 'create_skate'),
    path('signup/', views.SignUp.as_view(), name = 'sign_up'),
    path('signup/profile', views.CreateProfile.as_view(), name = 'create_profile'),
    path("logout/", auth_views.LogoutView.as_view(), name= 'logout'),
    path("login/", auth_views.LoginView.as_view(), name = 'login'),
    path('organize/', include('OrgDash.urls')),
    
 
    

]
