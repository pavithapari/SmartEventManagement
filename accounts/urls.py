from django.urls import path
from . import views

urlpatterns = [

    path("accounts/register/", views.register, name="register"),

    path("accounts/login/", views.login_view, name="login"),

    path("accounts/logout/", views.logout_view, name="logout"),

    path("accounts/dashboard/", views.dashboard, name="dashboard"),
    path("", views.home, name="home"),
    path("accounts/profile/", views.profile, name="profile"),
    path(
    "accounts/organizer-dashboard/",
    views.organizer_dashboard,
    name="organizer_dashboard",
),
]