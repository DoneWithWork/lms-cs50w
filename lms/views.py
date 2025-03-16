from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from lms.forms import CustomUserCreationForm
from lms.models import Course, User  # Import the custom form


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


def get_instructor(request, id):
    instructor = get_object_or_404(
        User.objects.only("id", "username", "email", "display_name"), id=id
    )
    return render(request, "lms/instructor.html", {"instructor": instructor})


""


def show_courses(request):
    name = request.GET.get("name")
    price = request.GET.get("price")
    print(name)
    courses = Course.objects.all()

    # Filter courses if 'name' parameter is provided
    if name:
        courses = courses.filter(title__icontains=name)

    return render(request, "lms/courses.html", {"courses": courses})


def cart(request):
    # Get the cookies
    pass


def show_account(request):
    pass
