# TODO POST vs GET in vote()
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import Event, Vote, User

app_name='listener'
def stay_tuned(request):
    return HttpResponse("Stay tuned for awesome progress")

def events(request):
    all_events = Event.objects.all()
    return render(request, 'listener/events.html', {'events':all_events})

class DetailView(generic.DetailView):
    model = Event
    template_name = 'listener/detail.html'

def testing(request):
    all_events = Event.objects.all()
    return render(request, 'listener/test.html', {'events':all_events})

def vote(request, event_id):
    # process POST requests only
    if request.method == "POST":
        # Raise error in case event does not exist 
        event = get_object_or_404(Event, pk=event_id)
        # map vote to number
        if request.POST.get('opinion') == "good":
            rating = 1
        else:
            rating = -1
        voter_id = request.POST.get("voter")
        # extract user id, if None leave it 
        try:
            voter = User.objects.get(pk=voter_id)
        except ObjectDoesNotExist:
            voter = None
    # MAGIC PART #
    vote_time = request.POST.get('vote_time')
    vote = Vote.objects.create(event=event, rating=rating,
                               vote_time=vote_time, voter=voter)
    vote.save()
    result = {}
    result['msg'] = "Vote created successfully"
    result['event_id'] = event_id
    result['rating'] = rating
    result['vote_time'] = request.POST.get('vote_time')
    result['voter_id'] = voter_id
    # Redirect to page that was raising the POST request
#    return HttpResponseRedirect(reverse('listener:detail', kwargs={'pk':event_id}))
    return HttpResponse(
        json.dumps(result),
        content_type="application/json"
    )

# quick and dirty to delete all posts
def votings(request):
    if request.method == "POST":
        all_votes = Vote.objects.all()
        all_votes.delete()
    return HttpResponseRedirect(reverse("listener:events"))
