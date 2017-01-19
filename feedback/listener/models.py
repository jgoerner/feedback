from django.db import models

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
