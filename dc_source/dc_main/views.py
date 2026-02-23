from django.shortcuts import render, redirect

from django.http import HttpRequest

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
def home_view(request:HttpRequest):
    return render(request, "dc_main/home.html")

def landing_view(request:HttpRequest):
    return render(request, "dc_main/landing_page.html")

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

@login_required
def user_profile_view(request:HttpRequest):
    return render(request, "dc_main/user-profile/user_profile.html")

@login_required
def user_details_view(request:HttpRequest):
    return render(request, "dc_main/user-profile/user_details.html")

@login_required
def user_preferences_view(request:HttpRequest):
    return render(request, "dc_main/user-profile/user_preferences.html")

def logout_view(request):
    logout(request)
    return redirect('home')