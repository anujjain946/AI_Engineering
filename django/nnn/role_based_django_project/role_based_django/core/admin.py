"""
Admin configuration for core app.
"""
from django.contrib import admin
from .models import MenuItem, RoleAssignment


@admin.register(RoleAssignment)
class RoleAssignmentAdmin(admin.ModelAdmin):
    list_display = ('role',)
    search_fields = ('role',)


class MenuItemInline(admin.TabularInline):
    model = MenuItem.roles.through
    extra = 1


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order', 'is_active', 'parent')
    list_filter = ('is_active', 'parent', 'roles')
    search_fields = ('title', 'url')
    ordering = ('order', 'title')
    list_editable = ('order', 'is_active')

    fieldsets = (
        (None, {
            'fields': ('title', 'url', 'icon', 'order', 'is_active', 'parent')
        }),
        ('Role Access', {
            'fields': ('roles',),
            'description': 'Leave empty to show to all roles'
        }),
    )
