from django.shortcuts import render, redirect
from django.contrib.auth import login
from lms.forms import CustomUserCreationForm  # Import the custom form


def index(request):
    return render(request, "lms/home.html")


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect("index")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {"form": form})
