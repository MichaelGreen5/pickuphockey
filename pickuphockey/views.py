from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from OrgDash.models import Skate, Player, Invitation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.db.models import Q
from pickuphockey.forms import SignUp
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from django.contrib.auth import login

def baseview(request):
    return render(request, 'base.html')




class SignUp(CreateView):
    form_class = SignUp
    success_url = reverse_lazy('OrgDash:organizer_dashboard')
    template_name = 'sign_up.html'

    def form_valid(self, form):
        request = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return request 


def Thanks(request):
    return render(request, 'thanks.html')



   



