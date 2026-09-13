from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Application Access", {"fields": ("is_admin_user",)}),
    )
    list_display = ("username", "email", "is_staff", "is_admin_user", "is_active")
    list_filter = ("is_staff", "is_admin_user", "is_active")
