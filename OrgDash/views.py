from django.shortcuts import render, redirect
from pickuphockey.models import Skate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, DeleteView
from OrgDash.forms import CreateEventForm
from django.db.models import Q
from django.urls import reverse_lazy


from django.utils import timezone




# Create your views here.

def OrganizerDashboard(request):
    today=timezone.now()
    active_user = request.user.pk
    todays_events = Skate.objects.filter(Q(host= active_user) & Q(time__date=today))
    upcoming_events = Skate.objects.filter(Q(host= active_user) & Q(time__gt= today))
    past_events = Skate.objects.filter(Q(host= active_user) & Q(time__lt= today))
    context = {'upcoming_events' : upcoming_events, 'past_events': past_events, 'todays_events': todays_events}
   

    return render (request,'OrgDash/dash_base.html',context)

class SkateCreateView(CreateView):
    template_name = 'OrgDash/create_event.html'
    success_url = reverse_lazy('OrgDash:organizer_dashboard')


    form_class= CreateEventForm
    model = Skate

class SkateDeleteView(DeleteView): #TODO make detail view, then give option to edit or delete inside detail view
    model = Skate
    template_name = 'OrgDash/confirm_delete.html'
    success_url = reverse_lazy('OrgDash:organizer_dashboard')

# def delete_object(request, id):
#     event = Skate.objects.get(id=id)
#     event.delete()
#     return redirect('OrgDash/dash_base.html')



class EventDetail(DetailView):
    model = Skate
    context_object_name = 'event'
    template_name = 'OrgDash/event_detail.html'
    
    