from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Student, Department, Course





@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('department_image', 'name', 'dec_code', 'description', "created_at", "updated_at")
    search_fields = ('name', 'dec_code', 'description')
    list_filter = ('name',)
    readonly_fields = (
        "dec_code",
        "created_at",
        "updated_at",
    )

    def department_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:5px;" />',
                obj.image.url
            )
        return "No Image"

    department_image.short_description = "Image"

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("course_image", 'name', 'course_code', 'description', 'department', "created_at", "updated_at")
    search_fields = ('name', 'course_code', 'description')
    list_filter = ('department',)
    readonly_fields = (
        "course_code",
        "created_at",
        "updated_at",
    )


    def course_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:5px;" />',
                obj.image.url
            )
        return "No Image"

    course_image.short_description = "Image"



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("student_image", 'name', 'student_code', 'email', 'course', "created_at", "updated_at")
    search_fields = ('name', 'student_code', 'email')
    list_filter = ('course',)
    ordering = ('name',)  #   "-name",  for descending order, use a minus sign before the field name
    readonly_fields = (
        "student_code",
        "created_at",
        "updated_at",
    )

   
    def student_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:5px;" />',
                obj.image.url
            )
        return "No Image"

    student_image.short_description = "Image"


# admin.site.register(Student)
# admin.site.register(Department)
# admin.site.register(Course)