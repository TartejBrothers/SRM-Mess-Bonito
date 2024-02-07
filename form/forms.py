from django import forms
from .models import Details
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, CharField


class add_data(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(add_data, self).__init__(*args, **kwargs)
        self.fields["lunch"].initial = "Yes"  # Set 'Yes' as the default for lunch
        self.fields["dinner"].initial = "Yes"  # Set 'Yes' as the default for dinner

        # Remove the empty option from the choices
        self.fields["lunch"].choices = [("Yes", "Yes"), ("No", "No")]
        self.fields["dinner"].choices = [("Yes", "Yes"), ("No", "No")]

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
