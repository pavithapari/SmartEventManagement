from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(forms.ModelForm):



    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Password"
            }
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Password"
            }
        )
    )

    class Meta:
        model = User

        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password"
        ]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Username"
            }),

            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter First Name"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Last Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Email"
            }),
        }

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class ProfileForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = [
            "phone_number",
            "department",
            "year"
        ]

        widgets = {
            "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Phone Number"
            }),

            "department": forms.Select(attrs={
                "class": "form-control"
            }),

            "year": forms.Select(attrs={
                "class": "form-control"
            }),
        }


class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Username"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Password"
            }
        )
    )