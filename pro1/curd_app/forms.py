from django import forms
from .models import College


class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "middle_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "college": forms.TextInput(attrs={"class": "form-control"}),
            "branch": forms.Select(),
            "date": forms.DateInput(attrs={"type": "date"})
        }
