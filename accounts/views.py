from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
                else:
                    messages.error(request, "Account not active")
            else:
                messages.error(request, "Please enter the correct username and password!")
    else:
        return redirect("home")
    return render(request, "accounts/login.html")

@login_required
def log_out(request):
    logout(request)
    return redirect("login")