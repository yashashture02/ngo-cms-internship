from django.shortcuts import render, redirect # type: ignore
from .models import Event


# 📌 SHOW ALL EVENTS
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


# 📌 ADD EVENT
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        event_date = request.POST.get('event_date')
        location = request.POST.get('location')

        Event.objects.create(
            title=title,
            description=description,
            event_date=event_date,
            location=location
        )

        return redirect('/events/')

    return render(request, 'events/add_event.html')


# 📌 EDIT EVENT
def edit_event(request, id):
    event = Event.objects.get(id=id)

    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.event_date = request.POST.get('event_date')
        event.location = request.POST.get('location')
        event.save()

        return redirect('/events/')

    return render(request, 'events/edit_event.html', {'event': event})

from django.shortcuts import render, redirect # type: ignore
from .models import Donation

def donate(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        message = request.POST.get("message")

        Donation.objects.create(
            name=name,
            amount=amount,
            message=message
        )

        return redirect('/events/')

    return render(request, 'events/donate.html')

# 📌 DELETE EVENT
def delete_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect('/events/')


# 📌 DONATION LIST (if you already started this)
def donation_list(request):
    return render(request, 'events/donations.html')


# 📌 DONATE PAGE
def donate(request):
    return render(request, 'events/donate.html')


# 📌 OPTIONAL (if you used this earlier)
def create_event(request):
    return redirect('/events/')