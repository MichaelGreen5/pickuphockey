from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from pickuphockey.models import Skate

# Create your views here.
def baseview(request):
    return render(request, 'base.html')


class SkateDetailView(DetailView):
    model = Skate
    template_name = 'tonights_skate.html'