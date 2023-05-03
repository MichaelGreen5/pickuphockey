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
from quickteams.views import QuickTeams, CreateQuickPlayer
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name = 'home'),
    path('signup/', views.SignUp.as_view(), name = 'sign_up'),
    path("logout/", auth_views.LogoutView.as_view(), name= 'logout'),
    path("login/", views.CustomLogin.as_view(), name = 'login'),
    path("thanks/", views.Thanks, name = 'thanks'),
    path('contact/', views.Contact, name = 'contact'),
    path('message-sent', views.MessageSent, name = 'message_sent'),
    path('how-it-works', views.HowItWorks, name = 'how_it_works'),

    

    path('reset-password/', views.PasswordReset.as_view(), name ='reset_password'),
    path('reset-password-sent/', views.PasswordResetSent.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', views.PasswordResetFormView.as_view(), name ='password_reset_confirm'),
    path('reset-password-complete/', views.PasswordResetComplete.as_view(), name ='password_reset_complete'),
    
    path('organize/', include('OrgDash.urls')), 
    path('quick_teams/', include('quickteams.urls'))

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls))
    ] + urlpatterns