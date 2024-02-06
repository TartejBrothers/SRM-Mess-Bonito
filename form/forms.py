from django import forms
from .models import Details
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, CharField


class add_data(forms.ModelForm):
    class Meta:
        model = Details
        fields = ["email", "lunch", "dinner"]
        widgets = {
            "email": EmailInput(
                attrs={
                    "class": "form-control",
                    "style": " background:#373737; margin-bottom:20px; border:none;width:calc(100% - 60px); font-size:16px;color: white; opacity:0.8; padding:5px 10px;  border-radius:10px",
                }
            ),
            "lunch": forms.Select(
                attrs={
                    "class": "form-control",
                    "style": " background:#373737; margin-bottom:20px; border:none;width:calc(100% - 60px); font-size:16px;color: white; opacity:0.8; padding:5px 10px;  border-radius:10px",
                },
                choices=(
                    ("Yes", "Yes"),
                    ("No", "No"),
                ),
            ),
            "dinner": forms.Select(
                attrs={
                    "class": "form-control",
                    "style": " background:#373737;width:calc(100% - 65px); margin-bottom:20px; border:none; font-size:16px;color: white; opacity:0.8; padding:5px 10px; border-radius:10px",
                },
                choices=(
                    ("Yes", "Yes"),
                    ("No", "No"),
                ),
            ),
        }
