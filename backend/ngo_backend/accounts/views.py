from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from events.models import Event

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user:
            login(request, user)

            if user.is_superuser:
                return redirect('/dashboard/admin/')
            elif user.is_staff:
                return redirect('/dashboard/staff/')
            else:
                return redirect('/dashboard/user/')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')


def admin_dashboard(request):
    return render(request, 'dashboard_admin.html', {
        'events': Event.objects.count()
    })


def staff_dashboard(request):
    return render(request, 'dashboard_staff.html')


def user_dashboard(request):
    return render(request, 'dashboard_user.html')