from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileForm


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