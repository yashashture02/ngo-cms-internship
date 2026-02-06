from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile

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
            full_name=full_name
        )

        return redirect("/admin/")

    return render(request, "register.html")
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/admin/")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("/login/")

from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def dashboard(request):
    return render(request, "dashboard.html")
