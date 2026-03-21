from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from events.models import Event


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')


def dashboard(request):
    user = request.user

    total_events = Event.objects.count()

    if user.is_superuser:
        role = "Admin"
    elif user.is_staff:
        role = "Staff"
    else:
        role = "User"

    return render(request, 'dashboard.html', {
        'role': role,
        'total_events': total_events,
        'total_donations': 0,
        'total_amount': 0
    })