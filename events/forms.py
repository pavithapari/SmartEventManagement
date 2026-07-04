from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ["organizer", "created_at"]

        widgets = {
            "event_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),
            "registration_deadline": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),
            "event_time": forms.TimeInput(
                attrs={
                    "type": "time",
                    "class": "form-control"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.setdefault("class", "form-control")