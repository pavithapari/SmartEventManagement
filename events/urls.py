from django.urls import path
from . import views

urlpatterns = [
     path("", views.event_list, name="event_list"),
    path("create/", views.create_event, name="create_event"),
    path("<int:id>/", views.event_detail, name="event_detail"),
    path("edit/<int:id>/", views.edit_event, name="edit_event"),
    path("delete/<int:id>/", views.delete_event, name="delete_event"),
]