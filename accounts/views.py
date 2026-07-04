from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileForm
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from events.models import Event
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from registrations.models import Registration
from .forms import UserUpdateForm, ProfileUpdateForm

from django.db.models import Count
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

    registrations = Registration.objects.filter(
        user=request.user,
        status="REGISTERED"
    )

    registered_count = registrations.count()

    upcoming_events = registrations.filter(
        event__event_date__gte=timezone.now().date()
    )

    past_events = registrations.filter(
        event__event_date__lt=timezone.now().date()
    )

    context = {

        "registered_count": registered_count,

        "upcoming_count": upcoming_events.count(),

        "past_count": past_events.count(),

        "my_upcoming_events": upcoming_events,

        "my_past_events": past_events,

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )

def home(request):

    upcoming_events = Event.objects.filter(
        event_date__gte=timezone.now().date()
    ).order_by("event_date")[:6]

    context = {
        "upcoming_events": upcoming_events,
    }

    return render(
        request,
        "home/home.html",
        context
    )
@login_required
def profile(request):
    return render(request, "accounts/profile.html")







@login_required
def organizer_dashboard(request):

    my_events = (
        Event.objects.filter(organizer=request.user)
        .annotate(total_registrations=Count("registrations"))
        .order_by("event_date")
    )

    context = {
        "my_events": my_events,
        "total_events": my_events.count(),
        "upcoming_events": my_events.filter(status="OPEN").count(),
        "total_registrations": sum(
            event.total_registrations
            for event in my_events
        ),
    }

    return render(
        request,
        "dashboard/organizer_dashboard.html",
        context,
    )




@login_required
def edit_profile(request):

    profile = request.user.profile

    if request.method == "POST":

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("profile")

    else:

        user_form = UserUpdateForm(
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            instance=profile
        )

    context = {

        "user_form": user_form,

        "profile_form": profile_form,

    }

    return render(
        request,
        "accounts/edit_profile.html",
        context
    )