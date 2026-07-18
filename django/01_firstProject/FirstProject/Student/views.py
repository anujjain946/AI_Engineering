from urllib import request
from django.shortcuts import render
from django.shortcuts import redirect
from .form import StudentForm


# Create your views here.

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student/student_form.html', {'form': form})


