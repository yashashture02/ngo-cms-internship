from django.shortcuts import render, redirect
from .models import Event, Donation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    total_events = Event.objects.count()
    total_donations = Donation.objects.count()
    total_amount = sum([d.amount for d in Donation.objects.all()])

    return render(request, 'events/home.html', {
        'total_events': total_events,
        'total_donations': total_donations,
        'total_amount': total_amount
    })


def events_page(request):
    query = request.GET.get('q')

    if query:
        events = Event.objects.filter(title__icontains=query)
    else:
        events = Event.objects.all()

    return render(request, 'events/events.html', {'events': events})


@login_required
def add_event(request):
    if request.method == "POST":
        Event.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            date=request.POST['date'],
            image=request.FILES.get('image')
        )
        return redirect('/events/')
    return render(request, 'events/add_event.html')


@login_required
def edit_event(request, id):
    event = Event.objects.get(id=id)

    if request.method == "POST":
        event.title = request.POST['title']
        event.description = request.POST['description']
        event.date = request.POST['date']

        if request.FILES.get('image'):
            event.image = request.FILES.get('image')

        event.save()
        return redirect(f'/event/{id}/')

    return render(request, 'events/edit_event.html', {'event': event})


def donate(request):
    if request.method == "POST":
        Donation.objects.create(
            name=request.POST['name'],
            amount=int(request.POST['amount']),  # 🔥 FIX
            message=request.POST['message']
        )
        return redirect('/')  # 🔥 goes to home → updates count

    return render(request, 'events/donate.html')


def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'events/event_detail.html', {'event': event})


# AUTH (keep for stability)
def login_user(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'events/login.html')


def register_user(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('/login/')
    return render(request, 'events/register.html')


def logout_user(request):
    logout(request)
    return redirect('/')