from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

app_name='listener'
def stay_tuned(response):
    return HttpResponse("Stay tuned for awesome progress")

def events(response):
    all_events = Event.objects.all()
    return render(response, 'listener/all_events.html', {'events':all_events})
