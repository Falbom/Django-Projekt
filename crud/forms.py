from .models import Group, Student
from django import forms

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["number", "type"]
        labels = {
            "number": "Numer",
            "type": "Typ"
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "group"]
        labels = {
            "first_name": "Imie",
            "last_name": "Nazwisko",
            "group": "Grupa"
        }