from django.shortcuts import render # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .models import Event

@login_required(login_url="/login/")
def event_list(request):
    events = Event.objects.all()
    return render(request, "events_list.html", {"events": events})
from .models import Donation

def donation_list(request):
    donations = Donation.objects.all()
    return render(request, "donations_list.html", {"donations": donations})
