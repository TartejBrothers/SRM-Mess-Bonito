from django import forms
from .models import Details
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, CharField


class add_data(forms.ModelForm):
    class Meta:
        model = Details
        fields = ["lunch", "dinner"]
        widgets = {
            "lunch": forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 50%; background:#3C3C3C; margin-bottom:10px; border:none; font-size:16px;color: white; opacity:0.8; padding:10px",
                },
                choices=(
                    ("Yes", "Yes"),
                    ("No", "No"),
                ),
            ),
            "dinner": forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 50%; background:#3C3C3C; margin-bottom:10px; border:none; font-size:16px;color: white; opacity:0.8; padding:10px",
                },
                choices=(
                    ("Yes", "Yes"),
                    ("No", "No"),
                ),
            ),
        }
