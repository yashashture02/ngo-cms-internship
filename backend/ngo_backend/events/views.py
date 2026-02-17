from django.contrib.auth.decorators import login_required # type: ignore
from django.shortcuts import render, redirect # type: ignore
from .models import Event, Donation
from .forms import EventForm


@login_required(login_url="/login/")
def event_list(request):
    events = Event.objects.all()
    return render(request, "events_list.html", {"events": events})


@login_required(login_url="/login/")
def donation_list(request):
    donations = Donation.objects.all()
    return render(request, "donations_list.html", {"donations": donations})


@login_required(login_url="/login/")
def create_event(request):
    if request.user.profile.role not in ["admin", "staff"]:
        return redirect("/dashboard/")

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/events/")
    else:
        form = EventForm()

    return render(request, "create_event.html", {"form": form})
from events.models import Event, Donation
from django.db.models import Sum # type: ignore

@login_required(login_url="/login/")
def dashboard(request):
    profile = request.user.profile

    total_events = Event.objects.count()
    total_donations = Donation.objects.count()
    total_amount = Donation.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        "total_events": total_events,
        "total_donations": total_donations,
        "total_amount": total_amount,
    }

    if profile.role == "admin":
        return render(request, "dashboard_admin.html", context)
    elif profile.role == "staff":
        return render(request, "dashboard_staff.html", context)
    else:
        return render(request, "dashboard_user.html", context)
