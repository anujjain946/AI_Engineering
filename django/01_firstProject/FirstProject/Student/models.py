from django.db import models

# Create your models here.
class Department(models.Model):
    # name
    name = models.CharField(max_length=100)
    #unique code
    dec_code = models.CharField(max_length=10, unique=True)
    #description
    description = models.TextField()

    def __str__(self):
            return self.name
    
class Course(models.Model):
    # name
    name = models.CharField(max_length=100)
    #unique code
    course_code = models.CharField(max_length=10, unique=True)
    #description
    description = models.TextField()
    #department
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
            return self.name
    
class Student(models.Model):
    # name
    name = models.CharField(max_length=100)
    #unique code
    student_code = models.CharField(max_length=10, unique=True)
    #email
    email = models.EmailField(unique=True)
    #course
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
            return self.name