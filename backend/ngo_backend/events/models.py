from django.db import models # type: ignore

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title
class Donation(models.Model):
    donor_name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.donor_name} - {self.amount}"
