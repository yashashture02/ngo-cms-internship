from django.shortcuts import render, redirect # type: ignore
from .models import Event, Donation


def home(request):
    total_events = Event.objects.count()
    total_donations = Donation.objects.count()

    total_amount = sum(d.amount for d in Donation.objects.all())

    return render(request, 'events/home.html', {
        'total_events': total_events,
        'total_donations': total_donations,
        'total_amount': total_amount
    })


def event_list(request):
    query = request.GET.get('q')

    if query:
        events = Event.objects.filter(title__icontains=query)
    else:
        events = Event.objects.all()

    return render(request, 'events/event_list.html', {'events': events})


def add_event(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('event_date')
        location = request.POST.get('location')

        # 🔥 FIX: check if title exists
        if title:
            Event.objects.create(
                title=title,
                description=description,
                event_date=date,
                location=location
            )
            return redirect('/events/')
        else:
            return render(request, 'events/add_event.html', {'error': 'Title is required'})

    return render(request, 'events/add_event.html')


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


def delete_event(request, id):
    Event.objects.get(id=id).delete()
    return redirect('/events/')


def donate(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")

        if name and amount:
            Donation.objects.create(
                name=name,
                amount=int(amount),
                message=request.POST.get("message")
            )
            return redirect('/events/')
        else:
            return render(request, 'events/donate.html', {'error': 'All fields required'})

    return render(request, 'events/donate.html')