from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from OrgDash.models import Skate, Player, Invitation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.db.models import Q
from pickuphockey.forms import SignUp, LoginForm, CustomPasswordResetForm
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.views.generic.edit import FormView

from django.contrib.auth import login, authenticate

def baseview(request):
    return render(request, 'base.html')

def homepage(request):
    return render(request, 'home.html')




class SignUp(CreateView):
    form_class = SignUp
    success_url = reverse_lazy('OrgDash:organizer_dashboard')
    template_name = 'sign_up.html'

    def form_valid(self, form):
        request = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return request 
    
class CustomLogin(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('OrgDash:player_dash')
    



class PasswordReset(PasswordResetView):
    template_name = 'registration/reset_password.html'
    form_class = CustomPasswordResetForm
    

class PasswordResetSent(PasswordResetDoneView):
    template_name = 'registration/password_reset_sent.html'
   

class PasswordResetFormView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_form.html'

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'registration/password_reset_done.html'

def Thanks(request):
    return render(request, 'thanks.html')



   



