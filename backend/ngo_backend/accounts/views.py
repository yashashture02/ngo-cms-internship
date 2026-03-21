from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from events.models import Event, Donation


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')


def dashboard(request):
    return render(request, 'accounts/dashboard.html', {
        'total_events': Event.objects.count(),
        'total_donations': Donation.objects.count(),
        'total_amount': sum(d.amount for d in Donation.objects.all())
    })