from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from events.models import Event
from .models import Registration


@login_required
def register_event(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    # Already registered?
    if Registration.objects.filter(
        user=request.user,
        event=event,
        status="REGISTERED"
    ).exists():

        messages.warning(
            request,
            "You are already registered for this event."
        )

        return redirect("event_detail", id=event.id)

    # Event closed?
    if event.status != "OPEN":

        messages.error(
            request,
            "Registration for this event is closed."
        )

        return redirect("event_detail", id=event.id)

    # Deadline passed?
    if timezone.now() > event.registration_deadline:

        messages.error(
            request,
            "Registration deadline has passed."
        )

        return redirect("event_detail", id=event.id)

    # Capacity full?
    registrations = Registration.objects.filter(
        event=event,
        status="REGISTERED"
    ).count()

    if registrations >= event.capacity:

        messages.error(
            request,
            "Event is full."
        )

        return redirect("event_detail", id=event.id)

    Registration.objects.create(
        user=request.user,
        event=event
    )

    messages.success(
        request,
        "Successfully registered!"
    )

    return redirect("event_detail", id=event.id)