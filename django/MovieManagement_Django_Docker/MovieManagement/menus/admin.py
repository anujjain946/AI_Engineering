from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        "name", "code", "url_name", "parent",
        "required_permission", "sort_order", "is_active"
    )
    list_filter = ("is_active",)
    search_fields = ("name", "code", "url_name", "required_permission")
    ordering = ("sort_order", "id")
