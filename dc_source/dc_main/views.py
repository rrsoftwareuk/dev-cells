from django.shortcuts import render, redirect

from django.http import HttpRequest

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Relationship

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

from .models import Action, Profile, performance_rating, dev_cell_rating, grade, potential_grade, position, location

# Create your views here.
def home_view(request:HttpRequest):
    return render(request, "dc_main/home.html")

def privacy_view(request:HttpRequest):
    return render(request, "dc_main/privacypolicy.html")


def login_view(request: HttpRequest):
    # Checks to see if the form was submitted and to save the values inputted as variables.
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Checking to see if the user exists and wether the password is correct.
        user = authenticate(request, username=username, password=password)

        # If user is found within the database and form inputs are correct, user is logged in and redirected to the home page.
        if user is not None:
            login(request, user)
            return redirect("home")
        # If user is not found within the database or user's form inputs are inncorrect compared to the database, error shown.
        else:
            context = {"error": "Invalid username or password"}
            return render(request, "dc_main/login.html", context)

    # Defult line that was used to close the function before.
    return render(request, "dc_main/login.html")


# Added a view for the signup page
def signup_view(request: HttpRequest):
    # Checks to see if the form was submitted and to save the values inputted as variables.
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        # Validating that password and confirm password match.
        if password != password2:
            return render(request, "dc_main/signup.html", {"error": "Passwords do not match"})

        # Checking to see if username already exists in the database.
        if User.objects.filter(username=username).exists():
            return render(request, "dc_main/signup.html", {"error": "Username already taken"})

        # Checking to see if email already exists in the databse.
        if User.objects.filter(email=email).exists():
            return render(request, "dc_main/signup.html", {"error": "Email already registered"})

        # Creates the user if form inputs are valid.
        user = User.objects.create_user(username=username, email=email, password=password)

        # Automatically logins the user in when account is created and redirected to the home page.
        login(request, user)
        return redirect("home")

    # Defult line that was used to close the function before.
    return render(request, "dc_main/signup.html")

def actions_view(request:HttpRequest):

    # Pulls the user and status values from the GET dicitonary

    status = request.GET.get("status", "all")
    username = request.GET.get("user", "all")

    # Selects all the user foreign keys in all action objects

    actions = Action.objects.select_related("user")


    # Filters action objects based on status and user, else it selects all

    if status != "all":
        actions = actions.filter(action_status=status)

    if username != "all":
        actions = actions.filter(user__username=username)
    
    context = {
        "actions" : actions,
        "users" : Profile.objects.all(),
        "selected_status" : status,
        "selected_user" : username
    }

    return render(request, "dc_main/actions_view.html", context)

@login_required
def user_profile_view(request:HttpRequest):
    return render(request, "dc_main/user-profile/user_profile.html")

@login_required
def user_details_view(request:HttpRequest):
    return render(request, "dc_main/user-profile/user_details.html")

@login_required
def user_preferences_view(request:HttpRequest):
    return render(request, "dc_main/user-profile/user_preferences.html")

@login_required
def account_deletion_view(request:HttpRequest):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        return redirect("home")
    
    return render(request, "dc_main/user-profile/account_deletion.html")

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def form_view(request: HttpRequest):

    profile = request.user.profile

    if request.method == "POST":
        profile.name = request.POST.get("name")
        profile.grade = request.POST.get("grade")
        profile.position = request.POST.get("position")
        profile.location = request.POST.get("location")
        profile.dev_cell_rating = request.POST.get("dev_cell_rating")
        profile.performance_rating = request.POST.get("performance_rating")
        profile.grade = request.POST.get("grade")
        profile.potential_grade = request.POST.get("potential_grade")

        print(profile.grade)
        print(profile.potential_grade)
        print(profile.position)
        print(profile.location)
        print(profile.dev_cell_rating)
        print(profile.performance_rating)

        profile.save()

        print("Saved!")
        
        return redirect("home")

    manager_relationship = Relationship.objects.filter(
        to_user=request.user,
        relationship_type="manager"
    ).select_related("from_user__profile").first()

    manager_name = ""
    if manager_relationship:
        manager_name = manager_relationship.from_user.profile.name

    performance_rating_options = performance_rating.objects.all()
    dev_cell_rating_options = dev_cell_rating.objects.all()
    potential_grade_options = potential_grade.objects.all()
    grade_options = grade.objects.all()
    location_options = location.objects.all()
    position_options = position.objects.all()

    context = {
        "username": profile.user.username,
        "name": profile.name,
        "manager": manager_name,
        "grade": profile.grade,
        "dev_cell_rating": profile.dev_cell_rating,
        "performance_rating": profile.performance_rating,
        "dev_cell_rating_options" : dev_cell_rating_options,
        "performance_rating_options" : performance_rating_options,
        "potential_grade" : potential_grade_options,
        "grade" : grade_options,
        "locations" : location_options,
        "positions" : position_options
    }

    return render(request, "dc_main/form.html", context)
