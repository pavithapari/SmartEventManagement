from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404
from .models import Event
from registrations.models import Registration
from .models import Event
from django.db.models import Q 

@login_required
def create_event(request):

    if request.method == "POST":

        form = EventForm(request.POST, request.FILES)

        if form.is_valid():

            event = form.save(commit=False)

            event.organizer = request.user

            event.save()

            return redirect("event_list")

    else:

        form = EventForm()

    context = {
        "form": form
    }

    return render(request, "events/create_event.html", context)

def event_list(request):
    events = Event.objects.all().order_by("event_date")
    search=request.GET.get("search")
    category=request.GET.get("category")
    if search:
        events=events.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(venue__icontains=search)
        )
    if category:
        events=events.filter(category=category)
    context = {
        "events": events,
        "search":search,
            "category":category,
        "categories":Event.CATEGORY_CHOICES,    }

    return render(request, "events/event_list.html", context)

def event_detail(request, id):

    event = get_object_or_404(Event, id=id)

    registered_count = event.registrations.filter(
        status="REGISTERED"
    ).count()

    seats_left = event.capacity - registered_count

    already_registered = False

    if request.user.is_authenticated:
        already_registered = Registration.objects.filter(
            user=request.user,
            event=event,
            status="REGISTERED"
        ).exists()

    context = {
        "event": event,
        "registered_count": registered_count,
        "seats_left": seats_left,
        "already_registered": already_registered,
    }

    return render(request, "events/event_detail.html", context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .models import Event
from .forms import EventForm


@login_required
def edit_event(request, id):

    event = get_object_or_404(Event, id=id)

    # Only the organizer can edit
    if event.organizer != request.user:
        messages.error(
            request,
            "You are not allowed to edit this event."
        )
        return redirect("event_detail", id=event.id)

    if request.method == "POST":

        form = EventForm(
            request.POST,
            request.FILES,
            instance=event
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Event updated successfully."
            )

            return redirect("event_detail", id=event.id)

    else:

        form = EventForm(instance=event)

    return render(
        request,
        "events/edit_event.html",
        {
            "form": form,
            "event": event,
        }
    )