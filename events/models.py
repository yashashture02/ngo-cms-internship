from django.db import models # type: ignore

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='events/', null=True, blank=True)  # 🔥 NEW

    def __str__(self):
        return self.title


class Donation(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name