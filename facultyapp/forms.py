from django import forms
from .models import CourseContent

class AddCourseForm(forms.ModelForm):
    class Meta:
        model= CourseContent
        fields="__all__"
