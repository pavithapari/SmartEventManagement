from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileForm
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register(request):

    if request.method == "POST":

        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save(commit=False)

            user.set_password(user_form.cleaned_data["password"])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect("login")

    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }

    return render(request, "accounts/register.html", context)
def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                messages.success(request, f"Welcome {user.first_name}!")

                return redirect("dashboard")

            else:

                messages.error(request, "Invalid Username or Password")

    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )


def logout_view(request):

    logout(request)

    messages.success(request, "Logged out successfully.")

    return redirect("login")
@login_required
def dashboard(request):

    return render(
        request,
        "dashboard/dashboard.html"
    )