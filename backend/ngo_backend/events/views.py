from django.shortcuts import render, redirect # type: ignore
from django.core.paginator import Paginator # type: ignore
from .models import Event, Donation


def event_list(request):
    event_list = Event.objects.all()
    paginator = Paginator(event_list, 3)

    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    return render(request, 'events/event_list.html', {'events': events})


def add_event(request):
    if request.method == "POST":
        Event.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            event_date=request.POST.get('event_date'),
            location=request.POST.get('location')
        )
        return redirect('/events/')

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
        Donation.objects.create(
            name=request.POST.get("name"),
            amount=int(request.POST.get("amount")),
            message=request.POST.get("message")
        )
        return render(request, 'events/donate.html', {'success': True})

    return render(request, 'events/donate.html')

def home(request):
    from .models import Event, Donation

    total_events = Event.objects.count()
    total_donations = Donation.objects.count()

    total_amount = 0
    for d in Donation.objects.all():
        total_amount += d.amount

    return render(request, 'events/home.html', {
        'total_events': total_events,
        'total_donations': total_donations,
        'total_amount': total_amount
    })