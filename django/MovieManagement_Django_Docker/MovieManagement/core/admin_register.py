from django.contrib import admin
from .admin_site import custom_admin_site
from accounts.models import User
from rbac.models import Role, Permission, RolePermission, UserRole
from menus.models import MenuItem

for model in [User, Role, Permission, RolePermission, UserRole, MenuItem]:
    try:
        admin.site.unregister(model)
    except admin.sites.NotRegistered:
        pass

@custom_admin_site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_admin_user", "is_active")
    search_fields = ("username", "email")

@custom_admin_site.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "is_active")

@custom_admin_site.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "is_active")

@custom_admin_site.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ("role", "permission")

@custom_admin_site.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "assigned_at")

@custom_admin_site.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "url_name", "required_permission", "sort_order", "is_active")
