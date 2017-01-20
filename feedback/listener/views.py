from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse
import json
from .models import Event, Vote

app_name='listener'
def stay_tuned(response):
    return HttpResponse("Stay tuned for awesome progress")

def events(response):
    all_events = Event.objects.all()
    return render(response, 'listener/events.html', {'events':all_events})

class DetailView(generic.DetailView):
    model = Event
    template_name = 'listener/detail.html'

def vote(response, event_id):
    # process POST requests only
    if response.method == "POST":
        # Raise error in case event does not exist 
        event = get_object_or_404(Event, pk=event_id)
        # map vote to number
        if response.POST.get('opinion') == "good":
            rating = 1
        else:
            rating = -1
    # MAGIC PART #
    vote = Vote.objects.create(event=event, rating=rating)
    vote.save()
    result = {}
    result['msg'] = "Vote created successfully"
    result['event_id'] = event_id
    result['rating'] = rating
    # Redirect to page that was raising the POST request
#    return HttpResponseRedirect(reverse('listener:detail', kwargs={'pk':event_id}))
    return HttpResponse(
        json.dumps(result),
        content_type="application/json"
    )

# quick and dirty to delete all posts
def votings(response):
    if response.method == "POST":
        all_votes = Vote.objects.all()
        all_votes.delete()
    return HttpResponseRedirect(reverse("listener:events"))
