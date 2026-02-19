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


@login_required(login_url="/login/")
def edit_event(request, id):
    if request.user.profile.role not in ["admin", "staff"]:
        return redirect("/dashboard/")

    event = Event.objects.get(id=id)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("/events/")
    else:
        form = EventForm(instance=event)

    return render(request, "edit_event.html", {"form": form})


@login_required(login_url="/login/")
def delete_event(request, id):
    if request.user.profile.role not in ["admin", "staff"]:
        return redirect("/dashboard/")

    event = Event.objects.get(id=id)
    event.delete()
    return redirect("/events/")
