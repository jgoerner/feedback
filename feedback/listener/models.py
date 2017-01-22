from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    # Event Attributes #
    event_name = models.CharField(max_length=100)
    event_htag = models.CharField(max_length=20)

    # Event Methods #
    def __str__(self):
        return self.event_name


class Vote(models.Model):
    # Reference to Event #
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.IntegerField()
    vote_time = models.DateTimeField(default=datetime.now, blank=True)
    voter = models.ForeignKey(User, default=-1)
