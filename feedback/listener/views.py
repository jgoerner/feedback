from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.views import generic

app_name='listener'
def stay_tuned(response):
    return HttpResponse("Stay tuned for awesome progress")

def events(response):
    all_events = Event.objects.all()
    return render(response, 'listener/events.html', {'events':all_events})

class DetailView(generic.DetailView):
    model = Event
    template_name = 'listener/detail.html'
