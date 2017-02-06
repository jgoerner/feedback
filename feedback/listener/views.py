# TODO POST vs GET in vote()
# TODO naming change "response" --> "request"
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse
import json
from .models import Event, Vote, User

app_name='listener'
def stay_tuned(response):
    return HttpResponse("Stay tuned for awesome progress")

def events(response):
    all_events = Event.objects.all()
    return render(response, 'listener/events.html', {'events':all_events})

class DetailView(generic.DetailView):
    model = Event
    template_name = 'listener/detail.html'

def testing(request):
    all_events = Event.objects.all()
    return render(request, 'listener/test.html', {'events':all_events})

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
        voter_id = response.POST.get("voter")
        # TODO change to PK of "anonymous"
        voter = get_object_or_404(User, pk=voter_id)
    # MAGIC PART #
    vote_time = response.POST.get('vote_time')
    vote = Vote.objects.create(event=event, rating=rating,
                               vote_time=vote_time, voter=voter)
    vote.save()
    result = {}
    result['msg'] = "Vote created successfully"
    result['event_id'] = event_id
    result['rating'] = rating
    result['vote_time'] = response.POST.get('vote_time')
    result['voter_id'] = voter_id
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
