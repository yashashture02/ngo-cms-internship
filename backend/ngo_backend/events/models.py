from django.db import models # type: ignore

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Donation(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name