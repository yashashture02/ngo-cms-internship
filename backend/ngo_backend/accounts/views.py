from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .models import Profile

from django.contrib.auth import authenticate, login, logout # type: ignore

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/dashboard/")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        full_name = request.POST.get("full_name")

        user = User.objects.create_user(
            username=username,
            password=password
        )

        Profile.objects.create(
            user=user,
            full_name=full_name,
            role="user"
        )

        return redirect("/login/")

    return render(request, "register.html")

@login_required(login_url="/login/") # type: ignore
def dashboard(request):
    profile = request.user.profile

    if profile.role == "admin":
        return render(request, "dashboard_admin.html")
    elif profile.role == "staff":
        return render(request, "dashboard_staff.html")
    else:
        return render(request, "dashboard_user.html")
