"""
Context processors for menu system.
"""
from django.db import models
from .models import MenuItem, RoleAssignment


def menu_processor(request):
    """
    Context processor to add menu items to all templates.
    Returns menu items filtered by user role.
    """
    if not request.user.is_authenticated:
        menu_items = MenuItem.objects.filter(is_active=True, parent__isnull=True, roles__isnull=True)
    else:
        user_role = request.user.role
        try:
            role_assignment = RoleAssignment.objects.get(role=user_role)
            menu_items = MenuItem.objects.filter(
                is_active=True,
                parent__isnull=True
            ).filter(
                models.Q(roles__isnull=True) | models.Q(roles=role_assignment)
            ).distinct()
        except RoleAssignment.DoesNotExist:
            menu_items = MenuItem.objects.filter(is_active=True, parent__isnull=True, roles__isnull=True)

    return {
        'menu_items': menu_items,
        'user_role': getattr(request.user, 'role', None) if request.user.is_authenticated else None,
    }
