from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404
from .models import Event
from registrations.models import Registration
from .models import Event

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

    context = {
        "events": events
    }

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