from django.shortcuts import render, redirect # type: ignore
from django.core.paginator import Paginator # type: ignore
from .models import Event, Donation


# SHOW EVENTS
def event_list(request):
    event_list = Event.objects.all()

    paginator = Paginator(event_list, 3)
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    return render(request, 'events/event_list.html', {
        'events': events
    })


# ADD EVENT
def add_event(request):
    if request.method == "POST":
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


# EDIT EVENT
def edit_event(request, id):
    event = Event.objects.get(id=id)

    if request.method == "POST":
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.event_date = request.POST.get('event_date')
        event.location = request.POST.get('location')
        event.save()

        return redirect('/events/')

    return render(request, 'events/edit_event.html', {'event': event})


# DELETE EVENT
def delete_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect('/events/')


# DONATION (ONLY ONE FUNCTION ✅)
def donate(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount"))
        message = request.POST.get("message")

        Donation.objects.create(
            name=name,
            amount=amount,
            message=message
        )

        return redirect('/events/')

    return render(request, 'events/donate.html')