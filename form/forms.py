from django import forms
from .models import Details
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, CharField


class add_data(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(add_data, self).__init__(*args, **kwargs)
        self.fields["lunch"].initial = "Yes"
        self.fields["dinner"].initial = "Yes"
        self.fields["lunch"].choices = [("Yes", "Yes"), ("No", "No")]
        self.fields["dinner"].choices = [("Yes", "Yes"), ("No", "No")]

    class Meta:
        model = Details
        fields = ["email", "lunch", "dinner"]
        widgets = {
            "email": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "SRM ID (AB1234)",
                    "style": "background:#ffffff; margin-bottom:20px; border: 1px solid #0000000;width:calc(100% - 150px); font-size:16px;color: black; opacity:1; padding:5px 10px;  border-radius:10px",
                },
            ),
            "lunch": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio",
                },
                choices=(
                    ("Yes", "Yes"),
                    ("No", "No"),
                ),
            ),
            "dinner": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio",
                },
                choices=(
                    ("Yes", "Yes"),
                    ("No", "No"),
                ),
            ),
        }
        labels = {
            "email": "STUDENT NETID",
        }
