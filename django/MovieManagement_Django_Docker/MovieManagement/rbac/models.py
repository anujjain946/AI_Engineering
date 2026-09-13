from django.conf import settings
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role_permissions")
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name="permission_roles")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["role", "permission"], name="unique_role_permission")
        ]

class UserRole(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_roles")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="user_roles")
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "role"], name="unique_user_role")
        ]

def user_has_permission(user, permission_code):
    if not user or not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    return RolePermission.objects.filter(
        role__user_roles__user=user,
        role__is_active=True,
        permission__code=permission_code,
        permission__is_active=True,
    ).exists()

def user_has_role(user, role_code):
    if not user or not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    return UserRole.objects.filter(
        user=user, role__code=role_code, role__is_active=True
    ).exists()
