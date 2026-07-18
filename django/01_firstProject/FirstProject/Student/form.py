from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #  fields = "__all__"
        # Select Specific Fields
        fields = ['name', 'student_code', 'email', 'course', 'image']