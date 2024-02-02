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
                    "style": " background:#000000; margin-bottom:10px; border:none;width:calc(100% - 70px); font-size:16px;color: white; opacity:0.8; padding:5px 10px; border-radius:10px",
                },
                choices=(
                    ("Yes", "Yes"),
                    ("No", "No"),
                ),
            ),
            "dinner": forms.Select(
                attrs={
                    "class": "form-control",
                    "style": " background:#000000;width:calc(100% - 75px); margin-bottom:10px; border:none; font-size:16px;color: white; opacity:0.8; padding:5px 10px; border-radius:10px",
                },
                choices=(
                    ("Yes", "Yes"),
                    ("No", "No"),
                ),
            ),
        }
