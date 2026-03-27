import django.shortcuts # type: ignore
from django.shortcuts import render, redirect # type: ignore
from .models import Event, Donation
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore

def home(request):
    total_events = Event.objects.count()
    total_donations = Donation.objects.count()

    total_amount = sum(d.amount for d in Donation.objects.all())

    context = {
        'total_events': total_events,
        'total_donations': total_donations,
        'total_amount': total_amount,
    }

    return django.shortcuts.render(request, 'events/home.html', context)


def events_page(request):
    events = Event.objects.all()
    return django.shortcuts.render(request, 'events/events.html', {'events': events})


@login_required
@login_required
def add_event(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        image = request.FILES.get('image')

        Event.objects.create(
            title=title,
            description=description,
            date=date,
            image=image
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
        return redirect('/events/') # type: ignore

    return django.shortcuts.render(request, 'events/edit_event.html', {'event': event})


def delete_event(request, id):
    Event.objects.get(id=id).delete()
    return redirect('/events/') # type: ignore

@login_required
def events_page(request):
    events = Event.objects.all()
    return render(request, 'events/events.html', {'events': events})


def donate(request):
    if request.method == "POST":
        name = request.POST['name']
        amount = request.POST['amount']
        message = request.POST['message']

        Donation.objects.create(name=name, amount=amount, message=message)
        return redirect('/') # type: ignore

    return django.shortcuts.render(request, 'events/donate.html')

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists(): # type: ignore
            return render(request, 'events/register.html', {'error': 'User already exists'}) # type: ignore

        user = User.objects.create_user(username=username, password=password) # type: ignore
        login(request, user) # type: ignore
        return redirect('/') # type: ignore

    return render(request, 'events/register.html') # type: ignore


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password) # type: ignore

        if user is not None:
            login(request, user) # type: ignore
            return redirect('/') # type: ignore
        else:
            return render(request, 'events/login.html', {'error': 'Invalid credentials'}) # type: ignore

    return render(request, 'events/login.html') # type: ignore


def logout_user(request):
    logout(request) # type: ignore
    return redirect('/') # type: ignore

def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'events/event_detail.html', {'event': event})