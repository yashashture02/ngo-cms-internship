from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore


def login_view(request):
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
from django.contrib.auth.decorators import login_required # type: ignore

@login_required(login_url="/login/")
def dashboard(request):
    profile = request.user.profile

    if profile.role == "admin":
        return render(request, "dashboard_admin.html")
    elif profile.role == "staff":
        return render(request, "dashboard_staff.html")
    else:
        return render(request, "dashboard_user.html")
def logout_view(request):
    logout(request)
    return redirect("/login/")