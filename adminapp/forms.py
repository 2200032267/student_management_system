from django import forms
from django.forms import ModelForm

from .models import Faculty,Student

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields ="__all__"
        exclude = {"password"}
        labels = {"facultyid":"enter faculty id","gender":"enter gender"}


class  AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = {"password"}

class  StudentForm(forms.ModelForm):
     class Meta:
        model = Student
        fields="__all__"
        exclude={"studentid"}



