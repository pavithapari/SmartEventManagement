from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm


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